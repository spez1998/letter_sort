# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:13:45 2020

@author: charl
"""

x = []
i = 4
prime = 10001
count = 0
while count <= prime-3:
    for j in range(2,int(i/2)+1):
        if i%j == 0:
            i = i + 1
            break
        else:
            if j == int(i/2):
                count = count + 1
                i = i + 1
print(i-1)
                
        
    