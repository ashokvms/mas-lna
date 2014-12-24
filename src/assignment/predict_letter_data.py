# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 10:55:03 2014

@author: ashok
"""

from sklearn import tree
import os
from IPython.core.display import Image
import matplotlib.pyplot as plt
import numpy as np

examples = []
nodes = []

example_size = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

for no_of_examples in example_size:
    features1 = features[0:no_of_examples-1, :]
    targets1 = labels[0:no_of_examples-1, :]
    
    clf1 = tree.DecisionTreeClassifier(criterion='entropy', splitter='best',\
    max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None,\
    random_state=None, min_density=None, compute_importances=None)
    
    clf1 = clf1.fit(features1, targets1)
    
#    with open("8.dot", 'w') as f:
#        f = tree.export_graphviz(clf1, out_file=f)
#    
#    file_name='../../docs/assignment/8_'+str(no_of_examples)+'.png'
#    os.system("dot -Tpng 8.dot -o "+file_name)
#    os.unlink('8.dot')
#    Image(filename=file_name)
    
    print str(no_of_examples)+' examples, learnt classes', clf1.tree_.n_classes
    print str(no_of_examples)+' examples, total number of nodes in the tree', clf1.tree_.node_count
    print
    examples.append(no_of_examples)
    nodes.append(clf1.tree_.node_count)

print 'Example set size ',examples
print 'Corresponding no. of nodes ', nodes
print
plt.plot(examples, nodes)
plt.xlabel("no_of_examples")
plt.ylabel("no_of_nodes")
plt.savefig('../../docs/assignment/8.png')

