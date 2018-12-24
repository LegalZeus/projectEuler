def arraySum(a):
  sum = 0
  for i in range(len(a)):
    sum += a[i]
  return sum

n = 10
state = True
exp = 5
a= []
while state:
  if n > 1000000:
    state = False
  sum = 0
  for i in range(0, len(str(n))):
    sum += int(str(n)[i])**exp

  if sum == n :
    print(n)
    a.append(n)
                  
                 
  n += 1

print(f"\n\nsum : {arraySum(a)}\n\n")
