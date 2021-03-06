# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:31:23 2018

@author: HPuser
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    copyL = L[:]
    del L[:]
    for i in range(len(copyL)):
        if (g(f(copyL[i])) == True):
            L.append(copyL[i])
    if (len(L) == 0):
        return -1
    else:
        return max(L)
def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0,5,4,4,4,4,4,4,4,4,4,4,0,9]
print(applyF_filterG(L, f, g))
print(L)