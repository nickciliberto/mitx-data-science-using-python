#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:11:43 2020

@author: nicholas
"""

def genPrimes():
    n = 2
    primes = []
    while True:
        for prime in primes:
            if n % prime == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 1

