#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:24:31 2020

@author: nicholas
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a<=b:
        x = a
    elif a>b:
        x = b
    while x > 1:
        if a%x == 0 and b%x == 0:
            break
        x -= 1
    return x
print(gcdIter(2,12))
print(gcdIter(6,12))
print(gcdIter(9,12))
print(gcdIter(17,12))