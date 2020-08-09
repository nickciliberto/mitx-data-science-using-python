#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:14:22 2020

@author: nicholas
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns a list of all the keys in aDict whose values appear exactly once
    '''
    occurenceDict = dictValues(aDict)
    keys = []
    for i in aDict:
        if occurenceDict[aDict[i]] == 1:
            keys.append(i)
    return keys

def dictValues(aDict):
    '''
    aDict: a dictionary
    returns a dictionary with all the values of aDict as keys and
    their occurences as values
    '''
    occurenceDict = {}
    for key in aDict:
        if aDict[key] in occurenceDict:
            occurenceDict[aDict[key]] += 1
        else:
            occurenceDict[aDict[key]] = 1
    return occurenceDict

#tests
aDict = {1:1, 2:3, 3:4, 4:2}

print(uniqueValues(aDict))