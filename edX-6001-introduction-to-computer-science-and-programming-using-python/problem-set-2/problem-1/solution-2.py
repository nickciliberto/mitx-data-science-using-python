#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:25:20 2020

@author: nicholas
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def bal_calc(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        monthly_payment = monthlyPaymentRate * balance
        unpaid_bal = balance - monthly_payment
        new_bal = unpaid_bal * (1+ annualInterestRate/12)
        balance = new_bal
    return balance


print(round(bal_calc(balance, annualInterestRate, monthlyPaymentRate),2))