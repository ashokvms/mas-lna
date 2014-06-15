# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/sau/.spyder2/.temp.py
"""
import numpy as np
import random
#from sklearn import tree
import os
from IPython.core.display import Image


###### reading data from file ##############
data_from_file = [i.strip().replace(' ', '').split(',') for i in open("../../data/istanbul_stock.csv").readlines()]

print data_from_file