# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:02:06 2020

@author: charl
"""
x = []
b = 600851475143 
m = b
n=2
a=1
while n <= int(b/2):

      if m%n == 0:
          x.append(n)
          a = a*n
          m = m/n 
          if a == b:
              break
      else:
          n = n + 1
print(max(x))
            