#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:59:08 2020

@author: nicholas
"""

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    import random
    
    same_color = 0
    for i in range(numTrials):
        bucket = [1, 1, 1, 1, 2, 2, 2, 2]
        choices = []
        for i in range(3):
            choice = random.choice(bucket)
            choices.append(choice)
            bucket.remove(choice)
        if len(set(choices)) == 1:
            same_color += 1
    return same_color/numTrials

print(drawing_without_replacement_sim(10000))
        

