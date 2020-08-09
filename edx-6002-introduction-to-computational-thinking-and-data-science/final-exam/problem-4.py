#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 21:15:31 2020

@author: nicholas
"""

import pylab

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """    
    longest_runs = []
    for i in range(numTrials):
        
        rolls = []
        for i in range(numRolls):
            rolls.append(die.roll())
        
        longest_run = 1
        current_run = 1
        for i in range(1, numRolls):
            if rolls[i] == rolls[i-1]:
                current_run += 1
            if rolls[i] != rolls[i-1] or i == numRolls - 1:
                if current_run > longest_run:
                    longest_run = current_run 
                current_run = 1
        longest_runs.append(longest_run)
        
    sum_of_runs = 0
    for run in longest_runs:
        sum_of_runs += run
    average_length = sum_of_runs/len(longest_runs)

    makeHistogram(longest_runs, 10, 'Length of Longest Run', 'Occurrences')
    return average_length