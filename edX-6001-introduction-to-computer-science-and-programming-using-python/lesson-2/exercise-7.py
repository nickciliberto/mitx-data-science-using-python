# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:08:15 2020

@author: nciliber
"""

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

iteration = 0
count = 0
for letter in 'hello, world':
    iteration += 1
    while iteration < 5:
        count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))

