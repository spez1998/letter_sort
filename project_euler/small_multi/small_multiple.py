# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:44:17 2020

@author: charl
"""
import numpy as np

x = list(range(1,21))
y = np.array([0]*21*21)
y.shape = (21,21)
print(sum(y[:,3]))
for i in x:
    b = i
    j = 2
    while j <= int(i):
        if b%j == 0:
            y[i,j] = y[i,j] + 1
            b = b/j
        else:
            j = j + 1
mult = 1
for a in range(2,21):
    power = max(y[:,a])
    print(a, power)
    mult = mult*(a**power)
print(mult)                
        
    

             

             
 