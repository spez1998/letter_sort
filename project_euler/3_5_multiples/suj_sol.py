# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:21:11 2020

@author: suj
"""

three_fives = []
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
            three_fives.append(n)
ans = sum(three_fives)
print(ans)
