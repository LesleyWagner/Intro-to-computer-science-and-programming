# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:24:37 2018

@author: HPuser
"""
s= 'abcdeeabc'
prevChar=''
result = ''
substring = ''
for char in s:
    if (substring == ''):
        substring = char
    elif ord(char) >= ord(prevChar):
        substring += char
    elif (len(substring) > len(result)):
        result = substring
        substring = char
    else: 
        substring = char
    if (len(substring) > len(result)):
        result = substring
    prevChar = char
print('longest substring in alphabetical order is: ' + result)
        
        