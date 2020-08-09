#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:37:15 2020

@author: nicholas
"""

d = {'one':1,'three':3,'five':5,'two':2,'four':4}
a = dict(sorted(d.items(), key=lambda x: x[1]))
print(a)
print(d)


b = ['asd', 'longtext', 'miadletext', 'aszljlasdjlkjlajkdjla']
print(sorted(b, key=lambda x: x[2], reverse=True))

aDict = {1:1, 3:3, 5:5, 2:2, 4:4}
bDict = dict(sorted(aDict.copy().items()))
print(bDict)
print(aDict)