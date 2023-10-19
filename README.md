# Using Adamic-Adar Index Algorithm to Predict Volunteer Collaboration: Less is More
This repository is the code of our work entitled "Using Adamic-Adar Index Algorithm to Predict Volunteer Collaboration: Less is More".

Please cite [our work](https://arxiv.org/abs/2308.13176v1) when using the code :)
```
@article{wu2023using,
  title={Using Adamic-Adar Index Algorithm to Predict Volunteer Collaboration: Less is More},
  author={Wu, Chao and Chen, Peng and Yin, Baiqiao and Lin, Zijuan and Jiang, Chen and Yu, Di and Zou, Changhong and Lui, Chunwang},
  journal={arXiv preprint arXiv:2308.13176},
  year={2023}
}
```

# Data
The involved data can be found at https://www.kaggle.com/competitions/MLSP2023-volunteers-02/data

# The related model GCN-GAN is as below:
# GCN-GAN

This repository provide a pytorch implemention for the GCN-GAN model proposed in "A Non-linear Temporal Link Prediction Model for Weighted Dynamic Networks" INFOCOM 2019, [[pdf]][1].

## Quick Start

Modify hyper-parameters in file ```config.yml```.

### Preprocess data
data use colab_test.csv

```
python preprocess2.py
```

### Train

```
python train.py
```

### Test

```
python test.py
```

[1]: https://arxiv.org/pdf/1901.09165.pdf
