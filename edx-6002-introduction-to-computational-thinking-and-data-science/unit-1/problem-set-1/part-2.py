#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:30:07 2020

@author: nicholas
"""

from ps1_partition import get_partitions


realcowsDict = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
shortcowsDict = {'Maggie': 3, 'Herman': 7, 'Betsy': 9}

def brute_force_cow_transport(cows,limit=10):
    possibleSolutions = []
    for trip in get_partitions(cows.copy().keys()):
        possibleSolutions.append(trip)
    for solution in sorted(possibleSolutions, key=len):
        validSolution = True
        for trip in solution:
            tripWeight = 0
            for cow in trip:
                tripWeight += cows[cow]
            if tripWeight > limit:
                validSolution = False
        if validSolution:
            return solution




print(brute_force_cow_transport(realcowsDict,10))