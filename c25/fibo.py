import math

phi = (1+ 5**.5)/2

def digNumber(n):
  if n == 1:
    return 1
  return math.ceil((n * math.log10(phi) - .5 * math.log10(5)))


n = 100
state = True
while state:
  if digNumber(n) == 1000:
    state = False
    print(f"\n\n{n}\n\n")
  else:
    n += 1
