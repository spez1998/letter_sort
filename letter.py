# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:55:29 2020

@author: charl
"""
import random
random.seed()
N=int(input("How many letters are there? "))
wrong = 0
for k in range(10000):
    n = []
    m = []
    for i in range(1,N+1):
        n.append(i)
        m.append(i)
    random.shuffle(n)
    count = 0
    for j in range(N):
        if n[j] == m[j]:
           count = count + 1
    if count == 0:
        wrong = wrong + 1
print("The probablity that all the letters are wrong is", (wrong/10000))
    