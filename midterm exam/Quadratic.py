# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:31:52 2018

@author: HPuser
"""

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # Your code here 
    return evalQuadratic(a1,b1,c1,x1) + evalQuadratic(a2,b2,c2,x2)