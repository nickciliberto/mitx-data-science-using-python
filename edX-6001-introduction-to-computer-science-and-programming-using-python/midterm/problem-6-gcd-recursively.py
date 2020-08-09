#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:14:22 2020

@author: nicholas
"""

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if b == 0:
        return a
    return gcd(b, a%b)

a = 72
b = 84
print(gcd(a,b))