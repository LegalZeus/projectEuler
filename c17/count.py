
def letterCount(n):
  rules = [0, 3, 3, 5, 4, 5, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 8, 9, 8, 8, 6]
  rules2 = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
  r = 0
  finished = False
  x = n
  while (finished == False):
    if x >= 100:
      if x%100 == 0 or x < 200:
        r += 0
      else:
        r += 3
      r += 7
      r += rules[int(str(x)[0])]
      x = x - 100*int(str(x)[0])
    if x == 0 :
      finished = True
      
    if x <= 20:
      r += rules[x]
      finished = True
      
    if x > 20 and x < 100:
      i = int(str(x)[0])
      r += rules2[i]
      x = x - i*10
  return r


r = 0
for x in range(1, 1000):
  count = letterCount(x)
  r += count
  print(f"{x} : {count}")
print(f"\n\n{r}")
  
