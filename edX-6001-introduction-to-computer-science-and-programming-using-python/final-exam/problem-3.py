#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:10:00 2020

@author: nicholas
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    n = 1
    counter = 0
    while counter <= k:
        if counter == k:
            return True
        else:
            counter += n
            n += 1
    return False
    
print(is_triangular(5), 5, False)
print(is_triangular(6), 6, True)
print(is_triangular(7), 7, False)
print(is_triangular(8), 8, False)
print(is_triangular(9), 9, False)
print(is_triangular(10), 10, True)