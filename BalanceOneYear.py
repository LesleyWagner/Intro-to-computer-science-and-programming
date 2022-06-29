# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:47:43 2018

@author: HPuser

Calculates remaining balance after one year
"""
months = 12
mIR = annualInterestRate / 12.0

while (months > 0):
    mMP = monthlyPaymentRate*balance
    mUB = balance - mMP
    balance = mUB + (mIR*mUB)
    months -= 1
print('Remaining balance: ' + str(round(balance, 2)))