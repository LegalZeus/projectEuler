def factorial(n):
  r = 1
  while n >= 1:
    r *= n
    n = n-1
  return r

n = 3
s = 0
while True:
  
  dgts = []
  for x in str(n):
    dgts.append(int(x))

    fs = 0
    for d in dgts:
      fs += factorial(d)

    if n == fs:
      s += n
      print(s)
  n += 1
