# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 10:12:29 2014

@author: ashok
"""

import numpy as np


# loading data from file
li = [i.strip().split(',') for i in open("../../data/zoo.data").readlines()]
data = np.array(li) # complete data set
names = data[:,0] # only labels
d = data[:, 1:names.size] # only features

# class definition as given in 'zoo.names' file
class0 = "aardvark, antelope, bear, boar, buffalo, calf,\
cavy, cheetah, deer, dolphin, elephant,\
fruitbat, giraffe, girl, goat, gorilla, hamster,\
hare, leopard, lion, lynx, mink, mole, mongoose,\
opossum, oryx, platypus, polecat, pony,\
porpoise, puma, pussycat, raccoon, reindeer,\
seal, sealion, squirrel, vampire, vole, wallaby,wolf".replace(' ', '').split(',')

class1 = "chicken, crow, dove, duck, flamingo, gull, hawk,\
kiwi, lark, ostrich, parakeet, penguin, pheasant,\
rhea, skimmer, skua, sparrow, swan, vulture, wren".replace(' ', '').split(',')

class2 = "pitviper, seasnake, slowworm, tortoise, tuatara".replace(' ', '').split(',')

class3 = "bass, carp, catfish, chub, dogfish, haddock,\
herring, pike, piranha, seahorse, sole, stingray, tuna".replace(' ', '').split(',')

class4 = "frog, frog, newt, toad".replace(' ', '').split(',')

class5 = "flea, gnat, honeybee, housefly, ladybird, moth, termite, wasp".replace(' ', '').split(',')

class6 = "clam, crab, crayfish, lobster, octopus,\
scorpion, seawasp, slug, starfish, worm".replace(' ', '').split(',')

# classes corresponding to labels
labels = []
for name in names:
    if name in class0:
        labels.append(0)
    elif name in class1:
        labels.append(1)
    elif name in class2:
        labels.append(2)
    elif name in class3:
        labels.append(3)
    elif name in class4:
        labels.append(4)
    elif name in class5:
        labels.append(5)
    elif name in class6:
        labels.append(6)

# features
features = np.zeros(d.shape)
for i in range(features.shape[0]):
    for j in range(features.shape[1]):
        features[i,j] = int(d[i,j])

# convert labels into array and stack them with features
labels = np.array(labels).reshape(np.size(features,0),1)
features = np.hstack((labels, features))
