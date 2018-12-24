





a = [0,1,2,3,4,5,6,7,8,9]
state = True

cicles = 0
while state :
  print(a)
  if cicles == 1000000:
    state = False
    print(f"\n\n\{a}\n\n")
  maxI = -1
  for i in range(0, len(a)-1):
    if a[i] < a[i+1]:
      maxI = i
    
  if maxI == -1:
    state = False

  maxJ = -1
  for j in range(0, len(a)):
    if a[maxI] < a[j]:
      maxJ = j

  a[maxI], a[maxJ] = a[maxJ], a[maxI]
  
  end = a[maxI+1:]
  end.reverse()
  a = a[0:maxI+1]
  a += end
  cicles += 1

print("\n\nfinished\n\n")
'''
end = a[1:]
end.reverse()
print(end)
a = list(set(a+end))
print(a)
'''

