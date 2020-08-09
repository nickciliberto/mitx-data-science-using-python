#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:54:32 2020

@author: nicholas
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    x = 0
    y = 0
    while True:
        if test(x):
            return x
        elif test(y):
            return y
        else:
            x += 1
            y -= 1

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def g(x):
    return x == 0
print(solveit(g))

def h(x):
    return x**3 == -1000000
print(solveit(h))