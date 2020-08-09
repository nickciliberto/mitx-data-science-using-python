#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:18:28 2020

@author: nicholas
"""
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTrue = 0
    for num in range(numTrials):
        if oneTrial():
            numTrue += 1
    return float(numTrue/numTrials)

def oneTrial():
    import random
    bucket = ['r', 'r', 'r', 'g', 'g', 'g']
    chosenBalls = []
    for i in range(3):
        choice = random.choice(bucket)
        chosenBalls.append(choice)
        bucket.remove(choice)
    if chosenBalls[0] == chosenBalls[1] and chosenBalls[1] == chosenBalls[2]:
        return True
    else:
        return False
    
print(noReplacementSimulation(100))