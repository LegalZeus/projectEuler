def cycles(n, d):
  x = n * 9
  z = x
  k = 1
  
  while z % d:
    z = z * 10 + x
    k += 1
  return k

assert cycles(1, 7) == 6
assert cycles(1, 3) == 1


d = 2

hd = 0
hc = 0

while d < 1000:
  print(d)
  if not d%2 == 0 and not d%5 == 0:
    c = cycles(1, d)
    if c > hc:
      hc = c
      hd = d
  d += 1
  

  

print(f"\n\n{hd}\n\n")
