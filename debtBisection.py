# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:51:15 2018

@author: HPuser

Calculates minimum constant payment to pay off debt with bisection.
Test Case 1:
"""
mIR = annualInterestRate / 12.0
low = (1/12)*balance
high = (balance*(1+mIR)**12)/12.0
prevResult = 0
while (True):
    result = round((low+high)/2, 2)
    if (int(100*prevResult) == int(100*result)):
        if (newBalance < 0):
            break
        else:
            result = round(result + 0.01, 2)
            break
    months = 12
    newBalance = balance
    while (months > 0): 
        mUB = newBalance - result
        newBalance = mUB + (mIR*mUB)
        months -= 1
    if (newBalance == 0):
        break
    elif (newBalance > 0):
        low = result
    elif (newBalance < 0):
        high = result
    prevResult = result
print('Lowest Payment: ' + str(result))