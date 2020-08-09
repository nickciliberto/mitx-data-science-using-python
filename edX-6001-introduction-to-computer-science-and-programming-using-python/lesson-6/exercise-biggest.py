#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:18:50 2020

@author: nicholas
"""

aDict = {'B': [15], 'u': [10, 15, 5, 2, 6]}

def biggest(aDict):
    biggest_value = []
    biggest_key = ''
    for key in aDict:
        if len(aDict[key]) > len(biggest_value):
            biggest_value = aDict[key]
            biggest_key = key
    return biggest_key

answer = biggest(aDict)

print(answer)