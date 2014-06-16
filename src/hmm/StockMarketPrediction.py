# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 22:42:04 2014

@author: saugata, ashok
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model


headers = []
ise_us = []
sp = []
dax = []
ftse = []
nikkei = []
bovespa = []
eu = []
em = []
features = []

###### reading data from file ##############
data_from_file = [i.strip().replace(' ', '').split(',') for i in open("../../data/istanbul_stock.csv").readlines()]

headers = data_from_file[0]

for i in range(1,537):
    ise_us = ise_us + [float(data_from_file[i][2])]
    sp = sp + [float(data_from_file[i][3])]
    dax = dax + [float(data_from_file[i][4])]
    ftse = ftse + [float(data_from_file[i][5])]
    nikkei = nikkei + [float(data_from_file[i][6])]
    bovespa = bovespa + [float(data_from_file[i][7])]
    eu = eu + [float(data_from_file[i][8])]
    em = em + [float(data_from_file[i][9])]

for i in range(0,536):
    features.append([sp[i],dax[i],ftse[i],nikkei[i],bovespa[i],eu[i],em[i]])

####################################################################################
########## feedback of outputs #####################################################

#no_of_prev_data_as_feature = 4
#
#features = np.array(features)
#out = np.array(ise_us).reshape(len(ise_us),1)
#
#
#
#
#targets = out[no_of_prev_data_as_feature:,:]
#
#prev_outputs = np.zeros((np.size(features,0)-no_of_prev_data_as_feature, no_of_prev_data_as_feature))
#
#for i in range(no_of_prev_data_as_feature, np.size(features, 0)):
#    prev_outputs[i-no_of_prev_data_as_feature,:] = out[i-no_of_prev_data_as_feature:i,0]
#    
#features = np.hstack((features[no_of_prev_data_as_feature:,:], prev_outputs))

#####################################################################################



test_set_ratio = 0.8

features = np.array(features)
targets = np.array(ise_us).reshape(len(ise_us),1)


#####################################################################################
######### Moving average ############################################################



#ewma = pandas.stats.moments.ewma
#
#fwd = ewma( features, span=20 ) 
#bwd = ewma( features[::-1], span=20 )
#
#features = (fwd+bwd)/2

####################################################################################


train_features = features[0:int(test_set_ratio*np.size(features,0)),:]
test_features = features[int(test_set_ratio*np.size(features,0)):,:]

train_targets = targets[0:int(test_set_ratio*np.size(features,0)),:]
test_targets = targets[int(test_set_ratio*np.size(features,0)):,:]



clf = linear_model.LinearRegression()
clf.fit(train_features, train_targets)
pred = clf.predict(test_features)

mse = np.sum((test_targets-pred)**2)
print mse
plt.plot(pred, label = 'predicted')
plt.plot(test_targets, label = 'actual')
plt.legend(loc = 8)





