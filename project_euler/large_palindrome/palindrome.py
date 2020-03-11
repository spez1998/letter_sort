# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:26:34 2020

@author: charl
"""

x = list(range(1,1000))
for i in x:
    if i%10 == 0:
        x.remove(i)
for n in range(1,999):
    numb = x[-n]*x[-n]
    r = list(str(numb))
    if len(r) == 5:
        if r[0] == r[-1] and r[1] == r[-2]:
            print(numb)
            break
    if len(r) == 6:
        if r[0] == r[-1] and r[1] == r[-2] and r[2] == r[-3]:
            print(numb)
            break
    numb = x[-n]*x[-(n+1)]
    r = list(str(numb))
    if len(r) == 5:
        if r[0] == r[-1] and r[1] == r[-2]:
            print(numb)
            break
    if len(r) == 6:
        if r[0] == r[-1] and r[1] == r[-2] and r[2] == r[-3]:
            print(numb)
            break
    
        
        

    