# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 22:42:04 2014

@author: ashok
"""

from __future__ import print_function

import numpy as np
from sklearn.hmm import GaussianHMM


print(__doc__)

features = np.array(features)
ise_us = np.array(ise_us)
em = np.array(em)

# pack diff and volume for training
X = np.column_stack([ise_us, features])

###############################################################################
# Run Gaussian HMM
print("fitting to HMM and decoding ...", end='')
n_components = 3

# make an HMM instance and execute fit
model = GaussianHMM(n_components, covariance_type="diag", n_iter=1000)

model.fit([X])

# predict the optimal sequence of internal hidden state
hidden_states = model.predict(X)

print("done\n")

###############################################################################
# print trained parameters and plot
print("Transition matrix")
print(model.transmat_)
print()

print("means and vars of each hidden state")
for i in range(n_components):
    print("%dth hidden state" % i)
    print("mean = ", model.means_[i])
    print("var = ", np.diag(model.covars_[i]))
    print()
