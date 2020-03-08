# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:55:29 2020

@author: charl
"""
import matplotlib.pyplot as plt
import random
random.seed()
from matplotlib import style


style.use('ggplot')
letters=int(input("How many letters are there? "))
tests=int(input("How many tests would you like to perform? Minimum is 1000. "))
if tests < 1000:
    tests = 1000
print("You have chosen to perform",tests,"tests on",letters,"letters.")
wrong = 0
for k in range(tests):
    n = []
    m = []
    for i in range(1,letters+1):
        n.append(i)
        m.append(i)
    random.shuffle(n)
    count = 0
    for j in range(letters):
        if n[j] == m[j]:
           count = count + 1
    if count == 0:
        wrong = wrong + 1
print("The probablity that all the letters are wrong is", (wrong/tests))
letters=int(input("How many letters are there? "))
x = list(range(100,10000,100))
y = []
for tests in x:
    wrong = 0
    for k in range(tests):
        n = []
        m = []
        for i in range(1,letters+1):
            n.append(i)
            m.append(i)
        random.shuffle(n)
        count = 0
        for j in range(letters):
            if n[j] == m[j]:
               count = count + 1
        if count == 0:
           wrong = wrong + 1
    y.append(wrong/tests)
plt.plot(x,y,'r')
plt.xlabel('Number of trials',fontsize=14)
plt.ylabel('Probability value',fontsize=14)
plt.show()
