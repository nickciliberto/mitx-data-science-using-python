#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:25:20 2020

@author: nicholas
"""

balance = 999999
annualInterestRate = 0.18

def remaining_bal(balance, annualInterestRate, monthly_payment):
    for i in range(12):
        unpaid_bal = balance - monthly_payment
        new_bal = unpaid_bal * (1+annualInterestRate/12)
        balance = new_bal
    return balance

low = balance/12
high = (balance * (1 + (annualInterestRate/12))**12)/12
guess = (low+high)/2

while True:
    z = remaining_bal(balance, annualInterestRate, guess)
    if round(z,2) == 0:
        break
    if round(z,2) > 0:
        low = guess
    if round(z,2) < 0:
        high = guess
    guess = (low+high)/2

print(round(guess,2))