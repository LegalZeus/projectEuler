p = "123456789"

n = 1
maxIt = 10000
it = 0
while True:
  if maxIt == it: break
  m = 1
  
  s = ""
  while len(s) < 9:
    #print(s)
    s += str(n*m)
    m += 1
    
  x = s
  if sorted(x) == sorted(p):
    print("\n\n", s, n)
    it = 0

  n += 1
  it += 1

print("\n\nFinished\n\n")
