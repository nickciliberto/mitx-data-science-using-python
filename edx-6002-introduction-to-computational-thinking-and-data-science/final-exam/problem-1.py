#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:11:51 2020

@author: nicholas
"""

import random

timesTrue = 0

x = 1000000

for i in range(x):
    bucket = ['r', 'r', 'r', 'r', 'b', 'b', 'b', 'b']
    selection = []
    for i in range(3):
        choice = random.choice(bucket)
        selection.append(choice)
        bucket.remove(choice)
    if selection[0] ==  selection[1] and selection[1] ==  selection[2]:
        timesTrue += 1

print(timesTrue/x)