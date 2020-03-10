# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:02:06 2020

@author: charl
"""
x = []
m = 24
for n in range(1,m):
    if m%n == 0:
        x.append(n)        
for i in range(len(x)):
    for a in range(2,x[i]):
        if x[i]%a == 0:
            x[i] = 0
            break
print(max(x))