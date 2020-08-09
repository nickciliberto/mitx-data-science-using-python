#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:24:31 2020

@author: nicholas
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr
    midindex = int(len(aStr)/2)
    midchar = aStr[midindex]
    if char == midchar:
        return True
    if char > midchar:
        return isIn(char, aStr[midindex+1:])
    if char < midchar:
        return isIn(char, aStr[:midindex])