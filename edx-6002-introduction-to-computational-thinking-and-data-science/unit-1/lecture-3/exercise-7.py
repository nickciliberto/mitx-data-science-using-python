#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:49:34 2020

@author: nicholas
"""

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    
    def getWeight(self):
        return self.weight

    def __str__(self):
        return '{}->{} ({})'.format(self.src, self.dest, self.getWeight())
