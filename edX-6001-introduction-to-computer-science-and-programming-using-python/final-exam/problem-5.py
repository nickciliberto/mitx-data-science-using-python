#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:36:39 2020

@author: nicholas
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    valuesDict = {}
    for key in aDict:
        valuesDict[aDict[key]] = valuesDict.get(aDict[key], 0) + 1
    
    keysList = []
    for key in aDict:
        if valuesDict[aDict[key]] == 1:
            keysList.append(key)
    return sorted(keysList)

print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
print(uniqueValues({1: 1, 2: 1, 3: 1}))