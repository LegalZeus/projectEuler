import math

def arraySum(a):
  r = 0
  for x in a:
    r +=  x
  return r


def divisors(n):
  r = []
  i = 1
  while(i < math.sqrt(n)):
    if n%i == 0:
      if n/i == i:
        r.append(i)
      else:
        r.append(i)
        r.append(n/i)
    i+= 1
  if n in r:
    r.remove(n)
    
  return r
sum = 0
lim = 10000
for i in range(1, lim):
  for j in range(1, lim):
    if divisors(i) == j and divisors(j) == 1:
      sum += i+j
      print(f"{i} = {j}")


print(sum)














