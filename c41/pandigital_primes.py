def isPrime(n: int) -> bool:
  if n <= 1 : return False
  if n <= 3 : return True

  if n%2 == 0 or n%3 == 0: return False

  i = 5
  while i*i <= n:
    if n%i == 0 or n%(i+2) == 0: return False
    i += 6
  return True


n = 1
maxIt = 100000
it = 0
while True:
  if it == maxIt : break
  if isPrime(n):
    
    p = ""
    for c in range(1, len(str(n))+1):
      p += str(c)

    x = str(n)
    if sorted(x) == sorted(p):
      it = 0
      print(f"\n{n}\n")
    else:
      it += 1
  n += 1


print("finished")
