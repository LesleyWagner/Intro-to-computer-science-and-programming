# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:42:57 2018

@author: HPuser
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here 
    result = []
    
    keys = aDict.keys()
    
    for key in keys:
        if (aDict[key] == target):
            result.append(key)
    result.sort()
    return result
