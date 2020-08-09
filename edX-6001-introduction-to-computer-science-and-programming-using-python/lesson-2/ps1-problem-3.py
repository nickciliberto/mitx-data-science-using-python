# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:33:56 2020

@author: nciliber
"""
final_answer = ''
temp_answer = ''
for letter in s:
    if not temp_answer:
        temp_answer = temp_answer + letter
        if len(temp_answer) > len(final_answer):
            final_answer = temp_answer
    elif letter >= temp_answer[-1]:
        temp_answer = temp_answer + letter
        if len(temp_answer) > len(final_answer):
            final_answer = temp_answer
    elif letter < temp_answer[-1]:
        temp_answer = ''
        temp_answer = temp_answer + letter
print(final_answer)