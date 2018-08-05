import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import os
from scipy.io import loadmat
from seqNMF import seq_nmf
from seqNMF import plot

data = loadmat(os.path.join('..', 'MackeviciusData.mat'))
W, H = seq_nmf(data['NEURAL'])

plot(W, H)

sns.heatmap(data)
