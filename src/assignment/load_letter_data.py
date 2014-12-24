# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 10:52:28 2014

@author: ashok
"""

import numpy as np

li = [i.strip().split(',') for i in open("../../data/letter-recognition.data").readlines()]

data = np.array(li)
labels = data[:,0]
d = data[:, 1:labels.size]

features = np.zeros(d.shape)
for i in range(features.shape[0]):
    for j in range(features.shape[1]):
        features[i,j] = int(d[i,j])
        
labels = np.array(labels).reshape(np.size(labels,0),1)