# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:23:04 2018

@author: HPuser
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if (N // 10 == 0):
        return N
    return sumDigits(N // 10) + N%10
print (str(sumDigits(83)))