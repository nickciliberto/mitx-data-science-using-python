#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:25:20 2020

@author: nicholas
"""

balance = 3329
annualInterestRate = 0.2

def remaining_bal(balance, annualInterestRate, monthly_payment):
    for i in range(12):
        unpaid_bal = balance - monthly_payment
        new_bal = unpaid_bal * (1+annualInterestRate/12)
        balance = new_bal
    return balance

monthly_payment = 10
while balance > 0:
    balance = remaining_bal(balance, annualInterestRate, monthly_payment)
    monthly_payment += 10

print(monthly_payment)