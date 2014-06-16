# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 23:27:30 2014

@author: sau
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/sau/.spyder2/.temp.py
"""
import numpy as np
import matplotlib.pyplot as plt


###### reading data from file ##############
#data_from_file = [i.strip().replace(' ', '').split(',') for i in open("../../data/istanbul_stock.csv").readlines()]

#print data_from_file

import pandas
ewma = pandas.stats.moments.ewma

# make a hat function, and add noise
x = np.linspace(0,1,100)



x = np.hstack((x,x[::-1]))

print x.shape

x += np.random.normal( loc=0, scale=0.1, size=200 )



plt.plot( x, alpha=0.4, label='Raw' )

#raw_input()


# take EWMA in both directions with a smaller span term
fwd = ewma( x, span=15 )          # take EWMA in fwd direction
bwd = ewma( x[::-1], span=15 )    # take EWMA in bwd direction
c = np.vstack(( fwd, bwd[::-1] )) # lump fwd and bwd together
c = np.mean( c, axis=0 )          # average

# regular EWMA, with bias against trend
plt.plot( ewma( x, span=20 ), 'b', label='EWMA, span=20' )

# "corrected" (?) EWMA
plt.plot( c, 'r', label='Reversed-Recombined' )

plt.legend(loc=8)
#savefig( 'ewma_correction.png', fmt='png', dpi=100 )