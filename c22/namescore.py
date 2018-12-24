
def strScore(s, i):
  alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  score = 0
  s = s.upper()
  for c in s:
    try:
      score += alfa.index(c) + 1
    except:
      score += 0
  return score*i




with open("names.txt", "r") as f:
  s = f.read()


s = s.replace('"', "")
a = s.split(",")
a.sort()
print(a)
sum = 0

for x in a:
  print(x)
  i = a.index(x)
  sum += strScore(x, i+1)


print(sum)
