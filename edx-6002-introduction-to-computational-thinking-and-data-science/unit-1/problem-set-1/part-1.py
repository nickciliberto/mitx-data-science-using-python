#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:30:07 2020

@author: nicholas
"""

def greedy_cow_transport(cows,limit=10):
    trips = []
    cowsDict = dict(sorted(cows.copy().items(), key=lambda x: x[1], reverse=True))
    while cowsDict:
        currentTrip = []
        currentWeight = 0
        for cow in cowsDict:
            if cowsDict[cow] + currentWeight <= limit:
                currentTrip.append(cow)
                currentWeight += cowsDict[cow]
        trips.append(currentTrip)
        for cow in currentTrip:
            del cowsDict[cow]
    return trips
