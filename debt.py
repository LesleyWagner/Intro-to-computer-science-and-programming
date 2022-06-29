# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:08:38 2018

@author: HPuser

Calculates minimum constant payment to pay off debt.
"""    
mIR = annualInterestRate / 12.0
mMP = int(10*(1 + (balance - balance/(mIR+1))//10))-10
newBalance = 1
while (newBalance > 0):
    newBalance = balance
    mMP += 10
    months = 12
    while (months > 0): 
        mUB = newBalance - mMP
        newBalance = mUB + (mIR*mUB)
        months -= 1
print('Lowest Payment: ' + str(mMP))