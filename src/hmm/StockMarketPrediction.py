# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 22:42:04 2014

@author: saugata, ashok
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.svm import NuSVR
from sklearn.linear_model import Ridge


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

##################################################

features = np.array(features)
targets = np.array(ise_us).reshape(len(ise_us),1)

####################################################################################
########## feedback of outputs #####################################################
def incorporate_feedback(data,targets,fb=4):
    mod_targets = targets[fb:,:]
    prev_outputs = np.zeros((np.size(mod_targets,0), fb))

    for i in range(np.size(features, 0)-fb):
        feedback = targets[i:i+fb,]
        for j in range(fb):
            prev_outputs[i,j] = feedback[j,:]
    
    mod_features = np.hstack((data[fb:,:], prev_outputs))
    return mod_features, mod_targets
#####################################################################################

####### incorporating feedback ############################
features, targets = incorporate_feedback(features, targets, 10)
###########################################################


########### normalizing ##########################################
features = np.divide((features-np.mean(features,0)),np.std(features,0))
targets = np.divide((targets-np.mean(targets,0)),np.std(targets,0))

print features.shape, targets.shape

test_set_ratio = 0.8

train_features = features[:int(test_set_ratio*np.size(features,0)),:]
test_features = features[int(test_set_ratio*np.size(features,0)):,:]

train_targets = targets[:int(test_set_ratio*np.size(features,0)),:]
test_targets = targets[int(test_set_ratio*np.size(features,0)):,:]


########### training ################
clf = linear_model.LinearRegression()
clf.fit(train_features, train_targets)

print 'accuracy on training set', clf.score(train_features,train_targets)
print 'accuracy on test set', clf.score(test_features,test_targets)

print 'mse on training set =', np.sum((train_targets-clf.predict(train_features))**2)/np.size(train_features,0)
print 'mse on test set =', np.sum((test_targets-clf.predict(test_features))**2)/np.size(test_features,0)

plt.figure(0)
plt.plot(clf.predict(train_features), label = 'predicted')
plt.plot(train_targets, label = 'actual')
plt.legend(loc = 8)
plt.title('Train set prediction')

plt.figure(1)
plt.plot(clf.predict(test_features), label = 'predicted')
plt.plot(test_targets, label = 'actual')
plt.legend(loc = 8)
plt.title('Test set prediction')

###############################################################
#### Support Vector Regression ################################
###############################################################
print '\nSupport Vector Regression\n'

targets = targets[:,0]
test_set_ratio = 0.8

train_features = features[:int(test_set_ratio*np.size(features,0)),:]
test_features = features[int(test_set_ratio*np.size(features,0)):,:]

train_targets = targets[:int(test_set_ratio*np.size(features,0))]
test_targets = targets[int(test_set_ratio*np.size(features,0)):]
########### training ################
clf = NuSVR(C=1.0, nu=0.1)
clf.fit(train_features, train_targets)

print 'accuracy on training set', clf.score(train_features,train_targets)
print 'accuracy on test set', clf.score(test_features,test_targets)

print 'mse on training set =', np.sum((train_targets-clf.predict(train_features))**2)/np.size(train_features,0)
print 'mse on test set =', np.sum((test_targets-clf.predict(test_features))**2)/np.size(test_features,0)

plt.figure(2)
plt.plot(clf.predict(train_features), label = 'predicted')
plt.plot(train_targets, label = 'actual')
plt.legend(loc = 8)
plt.title('Train set prediction')

plt.figure(3)
plt.plot(clf.predict(test_features), label = 'predicted')
plt.plot(test_targets, label = 'actual')
plt.legend(loc = 8)
plt.title('Test set prediction')


###############################################################
#### Support Vector Regression ################################
###############################################################
print '\nRidge for Regression\n'

########### training ################
clf = Ridge(alpha=1.0)
clf.fit(train_features, train_targets)

print 'accuracy on training set', clf.score(train_features,train_targets)
print 'accuracy on test set', clf.score(test_features,test_targets)

print 'mse on training set =', np.sum((train_targets-clf.predict(train_features))**2)/np.size(train_features,0)
print 'mse on test set =', np.sum((test_targets-clf.predict(test_features))**2)/np.size(test_features,0)

plt.figure(4)
plt.plot(clf.predict(train_features), label = 'predicted')
plt.plot(train_targets, label = 'actual')
plt.legend(loc = 8)
plt.title('Train set prediction')

plt.figure(5)
plt.plot(clf.predict(test_features), label = 'predicted')
plt.plot(test_targets, label = 'actual')
plt.legend(loc = 8)
plt.title('Test set prediction')

