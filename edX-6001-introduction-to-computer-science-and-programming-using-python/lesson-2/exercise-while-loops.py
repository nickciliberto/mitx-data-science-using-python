# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:37:29 2020

@author: nciliber
"""
end = int(input('Define end: '))
total = 0
current_num = 1
while current_num <= end:
    total += current_num
    current_num += 1
print(total)