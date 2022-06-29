# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:04:49 2018

@author: HPuser
"""

def longestRun(L):
    """    
    Arguments: L, a non-empty list of integers.
    Returns the length of the longest run of monotonically
    increasing numbers ocurring in L.
    """
    longest = 1
    run = 0
    for i in range(len(L)):
        if i==0:
            run += 1
        elif (L[i] >= L[i-1]):
            run += 1
        else:
            if (run>longest):
                longest = run
            run = 1
    if (run>longest):
        longest = run  
        
    return longest
                
#test
list = [5,4,3,2,1]
print( str(longestRun(list)))