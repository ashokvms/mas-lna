# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 10:31:08 2014

@author: ashok
"""

from sklearn import tree
import os
from IPython.core.display import Image

# Predicting attribute 18 from 2 to 17

features1 = features[:,1:16]
targets1 = features[:,17]

clf1 = tree.DecisionTreeClassifier(criterion='entropy', splitter='best',\
max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None,\
random_state=None, min_density=None, compute_importances=None)

clf1 = clf1.fit(features1, targets1)

with open("7_1.dot", 'w') as f:
    f = tree.export_graphviz(clf1, out_file=f)
    
os.system("dot -Tpng 7_1.dot -o ../../docs/assignment/7_1.png")
os.unlink('7_1.dot')
Image(filename='../../docs/assignment/7_1.png') 

# Predicting attribute 18 from 1 to 17

features2 = features[:,0:16]
targets2 = features[:,17]

clf2 = tree.DecisionTreeClassifier(criterion='entropy', splitter='best',\
max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None,\
random_state=None, min_density=None, compute_importances=None)

clf2 = clf2.fit(features2, targets2)

with open("7_2.dot", 'w') as f:
    f = tree.export_graphviz(clf2, out_file=f)

os.system("dot -Tpng 7_2.dot -o ../../docs/assignment/7_2.png")
os.unlink('7_2.dot')
Image(filename='../../docs/assignment/7_2.png') 

# Predicting attribute 6 from 5 to 5 and 7 to 18

features3 = np.hstack((features[:,1:4], features[:, 6:17]))
targets3 = features[:,5]

clf3 = tree.DecisionTreeClassifier(criterion='entropy', splitter='best',\
max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None,\
random_state=None, min_density=None, compute_importances=None)

clf3 = clf3.fit(features3, targets3)

with open("7_3.dot", 'w') as f:
    f = tree.export_graphviz(clf3, out_file=f)


os.system("dot -Tpng 7_3.dot -o ../../docs/assignment/7_3.png")
os.unlink('7_3.dot')
Image(filename='../../docs/assignment/7_3.png') 

# Predicting attribute 1 from 2 to 18

features4 = features[:,1:17]
targets4 = features[:,0]

clf4 = tree.DecisionTreeClassifier(criterion='entropy', splitter='best',\
max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None,\
random_state=None, min_density=None, compute_importances=None)

clf4 = clf4.fit(features4, targets4)

with open("7_4.dot", 'w') as f:
    f = tree.export_graphviz(clf4, out_file=f)


os.system("dot -Tpng 7_4.dot -o ../../docs/assignment/7_4.png")
os.unlink('7_4.dot')
Image(filename='../../docs/assignment/7_4.png') 