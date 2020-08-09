# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:13:41 2020

@author: nciliber
"""

def bal_calc(balance, annualInterestRate, monthlyPaymentRate):
    
    """
    Inputs: 
        balance int or float, initial account balance
        annualInterestRate float < 1 , annual interest rate
        monthlyPaymentRate float < 1 percentage of total balance that must be \
        paid each month as minimum balance
    Outputs:
        remaining balance after 12 months as float
        """
    
    monthly_interest_rate = annualInterestRate/12
    for month in range(12):
        
        # defines monthly_payment variable as monthly payment rate * balance
        monthly_payment = monthlyPaymentRate*balance
        
        #defines unpaid_bal as initial balance - monthly payment
        unpaid_bal = balance - monthly_payment
        
        #defines remaining balance as unpaid balance + interest
        remaining_bal = unpaid_bal * (1 + monthly_interest_rate)
        
        #resets balance as remaining balance for next iteration
        balance = remaining_bal
    
    #returns balance after 12 iterations rounded to 2 decimal places
    return round(balance,2)

#TEST
print(bal_calc(42, 0.2, 0.04))