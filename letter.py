# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:55:29 2020
@authors: charl and suj
"""
# Importing modules
import matplotlib.pyplot as plt
import random
from matplotlib import style

def shuffler(tests,letters):
    wrong = 0
    n = list(range(letters))
    m = list(range(letters))
    for k in range(tests):
        random.shuffle(n)
        count = 0
        for j in range(letters):
            if n[j] == m[j]:
               count += 1
        if count == 0:
           wrong += 1
    return wrong

def tester(wrong):
    random.seed()
    style.use('ggplot')
    letters=int(input("How many letters are there? "))
    x = list(range(100,10000,10))
    y = []
    for tests in x:
        wrong = shuffler(tests,letters)
        y.append(wrong/tests)
    plt.plot(x,y,'r')
    plt.xlabel('Trial number',fontsize=14)
    plt.ylabel('Probability',fontsize=14)
    plt.xscale("log")
    plt.show()

if __name__ == "__main__":
    tester(0)
