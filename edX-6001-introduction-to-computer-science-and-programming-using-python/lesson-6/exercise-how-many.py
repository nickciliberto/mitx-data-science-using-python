#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:18:50 2020

@author: nicholas
"""

aDict = {'B': [15], 'u': [10, 15, 5, 2, 6]}

def how_many(aDict):
    counter = 0
    for key in aDict:
        counter += len(aDict[key])
    return counter

print(how_many(aDict))