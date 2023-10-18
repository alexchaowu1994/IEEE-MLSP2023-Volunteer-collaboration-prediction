import pandas as pd
import numpy as np
import os
base_path ='/home/hbenke/Project/Yinbq/ybq/graph/data2'
data= pd.read_csv('/home/hbenke/Project/Yinbq/ybq/graph/data2/colab_test.csv')
tt=[]
for t in data.user_id.unique():
    tt.append(int(t))
tt.sort()
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/sort.txt','a+', encoding='utf-8') as f:
 for i in range (len(tt)):
  f.write((str(i)+'\t'+str(tt[i])+'\n'))
'''raw_base_path = os.path.join(base_path, 'time')
txt_path =  os.path.join(base_path, 'timetxt')
num = len(os.listdir(raw_base_path))
for i in range(num):
  with open(os.path.join(raw_base_path, str(i) +'_data' +  '.csv'), 'r') as f_in, open(os.path.join(txt_path, str(i) +'_data' +  '.txt'), 'w') as f_out:
    content = f_in.read().replace(',', ' ')
    f_out.write(content)'''

'''with open(os.path.join(txt_path, str(i) +'_data' +  '.txt'),'a+', encoding='utf-8') as f:
        for line in data.values:
            f.write((str(line[0])+'\t'+str(line[1])+'\t'+str(line[2])+'\n'))'''
'''
t=data.task_id.unique()
for index,row in data.iterrows():	
   
    if row['task_id'] not in time_dict:
        time_dict.update({row['task_id']:row['task_month']})
edge_dict = {}
data0 = {}
data1 = {}
data2 = {}
data3 = {}
data4 = {}
data5 = {}
data6 = {}
data7 = {}
data8 = {}
data9 = {}
data10 = {}
data11 = {}
data12 = {}
data13 = {}
data14 = {}
data15 = {}
data16 = {}
data17 = {}
data18 = {}
for t in data.task_id.unique():
    
    task = data[data.task_id==t]
    users = list(task.user_id.unique())
    edge_dict = {}
    # for each pairs of participants, create an edge
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            u, v = users[i], users[j]
            if (u, v) not in edge_dict and (v, u) not in edge_dict:
                edge_dict[(u, v)] = 1
            elif (u, v) in edge_dict:
                edge_dict[(u, v)] += 1
            else:
                edge_dict[(v, u)] += 1
    month=time_dict[t]
    for e, w  in edge_dict.items():
        if month==0:
            if (e[0],e[1]) not in data0:
                data0[(e[0],e[1])]=1
            else:
                data0[(e[0],e[1])]+=1
        elif month==1:
            if (e[0],e[1]) not in data1:
                data1[(e[0],e[1])]=1
            else:
                data1[(e[0],e[1])]+=1
        elif month==2:
            if (e[0],e[1]) not in data2:
                data2[(e[0],e[1])]=1
            else:
                data2[(e[0],e[1])]+=1
        elif month==3:
            if (e[0],e[1]) not in data3:
                data3[(e[0],e[1])]=1
            else:
                data3[(e[0],e[1])]+=1
        elif month==4:
            if (e[0],e[1]) not in data4:
                data4[(e[0],e[1])]=1
            else:
                data4[(e[0],e[1])]+=1
        elif month==5:
            if (e[0],e[1]) not in data5:
                data5[(e[0],e[1])]=1
            else:
                data5[(e[0],e[1])]+=1
        elif month==6:
            if (e[0],e[1]) not in data6:
                data6[(e[0],e[1])]=1
            else:
                data6[(e[0],e[1])]+=1
        elif month==7:
            if (e[0],e[1]) not in data7:
                data7[(e[0],e[1])]=1
            else:
                data7[(e[0],e[1])]+=1
        elif month==8:
            if (e[0],e[1]) not in data8:
                data8[(e[0],e[1])]=1
            else:
                data8[(e[0],e[1])]+=1
        elif month==9:
            if (e[0],e[1]) not in data9:
                data9[(e[0],e[1])]=1
            else:
                data9[(e[0],e[1])]+=1
        elif month==10:
            if (e[0],e[1]) not in data10:
                data10[(e[0],e[1])]=1
            else:
                data10[(e[0],e[1])]+=1
        elif month==11:
            if (e[0],e[1]) not in data11:
                data11[(e[0],e[1])]=1
            else:
                data11[(e[0],e[1])]+=1
        elif month==12:
            if (e[0],e[1]) not in data12:
                data12[(e[0],e[1])]=1
            else:
                data12[(e[0],e[1])]+=1
        elif month==13:
            if (e[0],e[1]) not in data13:
                data13[(e[0],e[1])]=1
            else:
                data13[(e[0],e[1])]+=1
        elif month==14:
            if (e[0],e[1]) not in data14:
                data14[(e[0],e[1])]=1
            else:
                data14[(e[0],e[1])]+=1
        elif month==15:
            if (e[0],e[1]) not in data15:
                data15[(e[0],e[1])]=1
            else:
                data15[(e[0],e[1])]+=1
        elif month==16:
            if (e[0],e[1]) not in data16:
                data16[(e[0],e[1])]=1
            else:
                data16[(e[0],e[1])]+=1
        elif month==17:
            if (e[0],e[1]) not in data17:
                data17[(e[0],e[1])]=1
            else:
                data17[(e[0],e[1])]+=1
        elif month==18:
            if (e[0],e[1]) not in data18:
                data18[(e[0],e[1])]=1
            else:
                data18[(e[0],e[1])]+=1

with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/0_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data0.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/1_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data1.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/2_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data2.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/3_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data3.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/4_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data4.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/5_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data5.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/6_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data6.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/7_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data7.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/8_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data8.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/9_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data9.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/10_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data10.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/11_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data11.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/12_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data12.items()]

with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/13_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data13.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/14_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data14.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/15_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data15.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/16_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data16.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/17_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data17.items()]
with open('/home/hbenke/Project/Yinbq/ybq/graph/data2/time/18_data.csv', 'w') as f:
    [f.write('{0},{1},{2}\n'.format(key[0],key[1], value)) for key, value in data18.items()]'''
'''
# add edges to the networkx graph
d=[]
for e, w  in edge_dict.items():
    np.append(d,[e[0],e[1],w],axis=0)
name=['id1','id2','w']
dd=pd.DataFrame(columns=name,data=d)
dd.to_csv ('/home/hbenke/Project/Yinbq/ybq/graph/data2/test_link.csv')
'''
# 再使用numpy保存为npy
#np.savetxt("/home/hbenke/Project/Yinbq/ybq/graph/data2/test_link.csv", data)'''