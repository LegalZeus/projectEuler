

def digits_sum(n):
  s = str(n)
  r = 0
  for i in range(len(s)):
    r += int(s[i])
    
  return r


o = digits_sum(2**1000)
print(o)
