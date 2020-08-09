# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:31:04 2020

@author: nciliber
"""

balance = 320000
annualInterestRate = 0.2


low = balance/12
high = (balance * (1 + annualInterestRate / 12) ** 12) / 12


def get_bal(balance, guess, air):
    for i in range(12):
        unpaid_bal = balance - guess
        balance = unpaid_bal * (1+(air/12))
    return balance

while True:
    guess = (low + high)/2 
    z = get_bal(balance, guess, annualInterestRate)
    if abs(round(z,2)) == 0:
        break
    if round(z, 2) < 0:
        high = guess
    if round(z, 2) > 0:
        low = guess

print(round(guess,2))