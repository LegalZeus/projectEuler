from math import *


def is_square(n):
  x = math.sqrt(n)
  if x**2 == n : return True
  else : return False


n = 100
s = {0}
for a in range(2, n+1):
  for b in range(2, n+1):
    x = a**b
    s = s.union(set({x}))

print(len(s)-1)
