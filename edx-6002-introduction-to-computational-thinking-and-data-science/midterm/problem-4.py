#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:33:43 2020

@author: nicholas
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    listOfSums = []
    for i in range(len(L)):
        for j in range(len(L)+1):
            if i < j:
                listOfSums.append(sum(L[i:j]))
            if i == j:
                listOfSums.append(L[i])
    return max(listOfSums)

a = [3, 4, -1, 5, -4]
b = [3, 4, -8, 15, -1, 2]
c = [1, 2, 3, 4, 5, 6]
d = [10, -9, 1, 2, 20, -100]
            

print(max_contig_sum(a))
print(max_contig_sum(b))
print(max_contig_sum(c))
print(max_contig_sum(d))