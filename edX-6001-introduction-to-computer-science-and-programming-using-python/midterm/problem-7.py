#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:14:22 2020

@author: nicholas
"""

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    for s in L[:]:
        if not f(s):
            L.remove(s)
    return len(L)

# =============================================================================
# run_satisfiesF(L, satisfiesF)
# 
# =============================================================================
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)