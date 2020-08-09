# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:18:54 2020

@author: nciliber
"""

s = 'azcbobobegghakl'
s = s.lower()
vowels = 'aeiou'
count = 0
for letter in s:
    if letter in vowels:
        count += 1
print(count)