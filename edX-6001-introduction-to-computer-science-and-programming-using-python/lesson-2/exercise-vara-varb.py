# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:45:02 2020

@author: nciliber
"""
varA = input('Enter varA ')
varB = input('Enter varB ')
x = 'a'
if type(varA) == type(x) or type(varB) == type(x):
    result = 'string involved'
elif varA > varB:
    result = 'bigger'
elif varA == varB:
    result = 'equal'
elif varA < varB:
    result = 'smaller'
print(result)