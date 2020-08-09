#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:15:02 2020

@author: nicholas
"""

balance = 320000
annualInterestRate = 0.2

def bal_calc(balance, annualInterestRate, monthlyPayment):
        
    """
    Inputs: 
        balance int or float, initial account balance
        annualInterestRate float < 1 , annual interest rate
        monthlyPayment payment made each month, must be int divisible by 10
    Outputs:
        remaining balance after 12 months as float
        """
        
    monthly_interest_rate = annualInterestRate/12
    for month in range(12):
            
        #defines unpaid_bal as initial balance - monthly payment
        unpaid_bal = balance - monthlyPayment
            
        #defines remaining balance as unpaid balance + interest
        remaining_bal = unpaid_bal * (1 + monthly_interest_rate)
            
        #resets balance as remaining balance for next iteration
        balance = remaining_bal
        
    #returns balance after 12 iterations rounded to 2 decimal places
    return balance

monthly_int_rate = annualInterestRate/12
low = balance/12
high = (balance * (1+monthly_int_rate)**12) / 12
guess = (low + high) / 2

while abs(round(bal_calc(balance, annualInterestRate, guess),2)) != 0:
    z = bal_calc(balance, annualInterestRate, guess)
    if round(z,2) == 0:
        break
    elif round(z,2) < 0:
        high = guess
    elif round(z,2) > 0:
        low = guess
    guess = (low + high) / 2

print(round(guess,2))