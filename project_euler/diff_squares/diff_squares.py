# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:03:32 2020

@author: charl
"""

x = 0
y = 0
for i in range(1,101):
    x = x + i**2
    y = y + i
print(y**2-x)
    