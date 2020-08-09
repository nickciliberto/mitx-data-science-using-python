#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:24:31 2020

@author: nicholas
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
print(gcdRecur(2,12))
print(gcdRecur(6,12))
print(gcdRecur(9,12))
print(gcdRecur(17,12))