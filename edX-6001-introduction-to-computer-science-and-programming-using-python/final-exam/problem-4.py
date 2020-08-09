#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:36:34 2020

@author: nicholas
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    decCount = 0
    incCount = 0
    maxCount = 0
    for i in range(len(L)-1):
        num = L[i]
        if num <= L[i+1]:
            incCount += 1
            if incCount > maxCount:
                maxCount = incCount
                maxPos = i+1
        else:
            incCount = 0
        if num >= L[i+1]:
            decCount += 1
            if decCount > maxCount:
                maxCount = decCount
                maxPos = i+1
        else:
            decCount = 0
    startPos = maxPos - maxCount
    result = 0
    for x in range(startPos, maxPos+1):
        result += L[x]
    return result