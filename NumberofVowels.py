# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:21:36 2018

@author: HPuser
"""

s='Hey there'
numvowels=0
for char in s:
    if (char == 'a' or char == 'e' or char == 'i' or char =='o' or char =='u'):
        numvowels +=1
numvowels = str(numvowels)
print('Number of vowels: ' + numvowels) 