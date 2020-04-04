# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:25:26 2020

@author: charl
"""

x = list(range(1,999))
for a in x:
    y = list(range(a,999))
    for b in y:
        c = (a**2 + b**2)**0.5
        if c%1 == 0:
            if a + b + c == 1000:
                print(a,b,c)
                break
