#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:02:50 2020

@author: nicholas
"""

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 0
    foundNumber = False
    while not foundNumber:
        if isMyNumber(guess) == 0:
            foundNumber = True
            return guess
            break
        elif isMyNumber(guess) == -1:
            guess += 1
        elif isMyNumber(guess) == 1:
            guess -= 1