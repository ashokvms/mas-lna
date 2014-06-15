# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 22:42:04 2014

@author: saugata, ashok
"""

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
