#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:04:52 2020

@author: nicholas
"""

import pylab

x_vals = []
linear = []
quadratic = []
cubic = []
exponential = []

for i in range(30):
    x_vals.append(i)
    linear.append(i)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.5**i)
    

pylab.figure('linear')
pylab.xlabel('sample points')
pylab.ylabel('linear values')
pylab.title('Linear Graph')
pylab.plot(x_vals, linear, label = 'linear')
pylab.legend(loc = 'upper right')

pylab.figure('quadratic')
pylab.xlabel('sample points')
pylab.ylabel('quadratic values')
pylab.title('Quadratic Graph')
pylab.plot(x_vals, quadratic, label = 'quadratic')
pylab.legend()

pylab.figure('cubic')
pylab.xlabel('sample points')
pylab.ylabel('cubic values')
pylab.title('Cubic Graph')
pylab.plot(x_vals, cubic, label = 'cubic')

pylab.figure('exponential')
pylab.xlabel('sample points')
pylab.ylabel('exponential values')
pylab.title('Exponential Graph')
pylab.plot(x_vals, exponential, label = 'exponential')

pylab.figure('linear')
pylab.figure('quadratic')
pylab.figure('cubic')
pylab.figure('exponential')

