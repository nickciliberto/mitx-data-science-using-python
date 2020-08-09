# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('Please think of a number between 0 and 100!')
high = 100
low = 0
guess = 50
correct = False
while not correct:
    print('Is your secret number', guess, '?')
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' \
                     to indicate the guess is too low. Enter 'c' to indicate I\
                     guessed correctly. ")
    if response == 'l':
        low = guess
        guess = int((high+low)/2)
    elif response == 'h':
        high = guess
        guess = int((high+low)/2)
    elif response == 'c':
        correct = True
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was:',guess)