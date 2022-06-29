# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:59:27 2018

@author: HPuser

Sums the area and perimeter of a polygon 
"""

from math import *

def polysum( n, s ):
    def area( n, s ):
        return (0.25*n*s**2)/(tan(pi/n))
    def perimeter( n, s ):
        return n*s
    return round(area( n, s ) + (perimeter( n, s ))**2, 4)