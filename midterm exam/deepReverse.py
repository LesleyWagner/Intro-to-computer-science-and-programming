# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:38:33 2018

@author: HPuser
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    L.reverse()
    
    for el in L:
        el.reverse()
    print(L)
deep_reverse ([[1, 2], [3, 4], [5, 6, 7]])