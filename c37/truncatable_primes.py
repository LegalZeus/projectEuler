def isPrime(n: int) -> bool:
  if n <= 1 : return False
  
  if n <= 3 : return True

  if n%2 == 0 or n%3 == 0: return False

  i = 5
  while i*i <= n:
    if n%i == 0 or n%(i+2) == 0: return False
    i += 6
  return True



def isTruncatableRt(n: int) -> bool:
  state = True
  x = n
  it = 1
  while it <= len(str(n)):
    
    if isPrime(int(x)): x = str(x)[:-1]
    else: return False
    it += 1
    
  return True

def isTruncatableLt(n : int) -> bool:
  x = n
  it = 1
  while it <= len(str(n)):

    if isPrime(int(x)) : x = str(x)[1:]
    else: return False
    it += 1
  return True

l = 0
n = 10
sum = 0
while l < 11:
  if isPrime(n):
    if isTruncatableLt(n) and isTruncatableRt(n):
      sum += n
      l += 1
      print(n, sum)
  n += 1
print(f"\n\n sum : {sum}\n\n")


