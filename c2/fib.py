import math


def isPerfectSqr(n):
  s = int(math.sqrt(n))
  return s*s == n

def isFibonacci(n):

  return isPerfectSqr(5*n*n+4) or isPerfectSqr(5*n*n - 4)






sum = 0
for n in range(1, 4000000):
  if n%2 == 0:
    if isFibonacci(n):
      print(sum)
      
      sum += n

print(f"\n\nsum: {sum}") 
