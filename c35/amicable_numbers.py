def isPrime(n : int) -> bool:
  if n <= 1: return False
  if n <= 3: return True

  if n%2 == 0 or n%3 == 0: return False

  i = 5
  while i*i <= n:
    if n%i == 0 or n%(i+2) == 0: return False
    i +=6
  return True

def rotations(x):
  N = []
  for q in list(str(x)):
    N.append(int(q))
  return [N[i:] + N[:i] for i in range(len(N))]

leng = 0
for n in range(1, 1000000):
  p = rotations(n)

  ns = []
  for x in p:
    s = ""
    for y in x:
      s += str(y)
    ns.append(int(s))

  primes = list(filter(lambda x: isPrime(x), ns))
  if ns == primes:
    print(n)
    leng += 1
print(f"\n\nlength : {leng}\n\n")






















  
