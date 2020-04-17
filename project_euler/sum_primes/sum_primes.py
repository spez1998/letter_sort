# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:46:45 2020

@author: charl
"""

x = list(range(2,200000))
print(2)
for a in x:
    for b in range(2,a):
        if a%b != 0:
            if b == a-1:
                print(a)
        else:
            break
      
        
    