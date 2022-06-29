# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:52:21 2018

@author: HPuser
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    n=1 #integer part of summation
    while k > 0:
        k -= n
        n += 1
    if (k==0):
        return True
    else:
        return False
 
#Test
result = is_triangular(9)
print(result)