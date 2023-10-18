import torch
from torch.utils.data import Dataset
import numpy as np
import pandas as pd

def get_snapshot(path, node_num, max_thres):
    file = open(path, 'r', encoding='utf-8')
    snapshot = np.zeros(shape=(node_num, node_num), dtype=np.float32)
    data= pd.read_csv('/home/hbenke/Project/Yinbq/ybq/graph/data2/colab_test.csv')
    tt=[]
    for t in data.user_id.unique():
        tt.append(int(t))
    tt.sort()
    with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/sort.txt','a+', encoding='utf-8') as f:
     for i in range (len(tt)):
      f.write((str(i)+'\t'+str(tt[i])+'\n'))
    node1=0
    node2=0
    for line in file.readlines():
        line = line.strip().split(' ')
        nod1 = int(line[0])
        nod2 = int(line[1])
        for i in range (len(tt)):
            if tt[i]==nod1:
                node1=i
            elif tt[i]==nod2:
                node2=i
        edge = float(line[2])
        edge = min(edge, max_thres)
        snapshot[node1, node2] = edge
        snapshot[node2, node1] = edge
    snapshot /= max_thres
    return snapshot

class LPDataset(Dataset):

    def __init__(self, path, window_size):
        super(LPDataset, self).__init__()
        self.data = torch.from_numpy(np.load(path))
        self.window_size = window_size
        self.num = self.data.size(0) - window_size

    def __len__(self):
        return self.num

    def __getitem__(self, item):
        return self.data[item: item + self.window_size], self.data[item + self.window_size]

def MSE(input, target):
    num = 1
    for s in input.size():
        num = num * s
    return (input - target).pow(2).sum().item() / num

def EdgeWiseKL(input, target):
    num = 1
    for s in input.size():
        num = num * s
    mask = (input > 0) & (target > 0)
    input = input.masked_select(mask)
    target = target.masked_select(mask)
    kl = (target * torch.log(target / input)).sum().item() / num
    return kl

def MissRate(input, target):
    num = 1
    for s in input.size():
        num = num * s
    mask1 = (input > 0) & (target == 0)
    mask2 = (input == 0) & (target > 0)
    mask = mask1 | mask2
    return mask.sum().item() / num