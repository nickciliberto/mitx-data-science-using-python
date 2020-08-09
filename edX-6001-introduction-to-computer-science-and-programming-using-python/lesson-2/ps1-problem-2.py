# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:18:54 2020

@author: nciliber
"""
search = 'bob'
count = 0
for i in range(len(s)):
    if search in s[i:i+3]:
        count += 1
print(count)