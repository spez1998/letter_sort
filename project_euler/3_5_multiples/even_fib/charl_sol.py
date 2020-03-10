a = 0
n = 0
m = 1
while m < 4000000:
      n = m+n
      m = n+m
      if m >= 4000000:
          break
      if n%2 == 0:
         a = a +n
      if m%2 == 0 :
         a = a + m
print(a)
    