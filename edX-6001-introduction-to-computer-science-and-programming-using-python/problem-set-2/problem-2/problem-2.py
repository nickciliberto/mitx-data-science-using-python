# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:13:41 2020

@author: nciliber
"""

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
    return round(balance,2)

balance = 3329
annualInterestRate = 0.2

lowest_payment = 10
while bal_calc(balance, annualInterestRate, lowest_payment) > 0:
    lowest_payment += 10
print(lowest_payment)