from math import sqrt, floor 

def isPenta(n):
  k = (sqrt(24*n+1)+1)/6
  return k.is_integer()

def isTriangular(num): 
  
  if (num < 0): 
    return False
         
  c = (-2 * num) 
  b, a = 1, 1
  d = (b * b) - (4 * a * c) 
  
  if (d < 0): 
    return False
   
  root1 = ( -b + sqrt(d)) / (2 * a) 
  root2 = ( -b - sqrt(d)) / (2 * a) 
   
  if (root1 > 0 and floor(root1) == root1): 
    return True
   
  if (root2 > 0 and floor(root2) == root2): 
    return True
  
  return False

def isHexa(x):
  ans = (sqrt(8 * x + 1) + 1) / 4
  return ans.is_integer()




n = 40755+1
while True:
  print(n)
  if isTriangular(n) and isPenta(n) and isHexa(n):
    print(f"****\n\n{n}\n\n****")
    break
  n += 1