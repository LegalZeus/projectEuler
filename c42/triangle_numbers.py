from math import sqrt

def removeQuotes(s : str) -> str:
  s = s.replace('"', "")
  return s

def isSquare(n: int) -> bool:
  x = sqrt(n)
  if x**2 == n: return True
  else: return False


def isTriangular(n: int) -> bool:
  if (sqrt(1+ 8*n)-1)/2 % 1 == 0: return True
  else: return False

alfa = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"


with open("data.txt", "r") as f:
  words = [line.split(",") for line in f.read().split("\n")]
words = words[0]

for i in range(len(words)):
  words[i] = removeQuotes(words[i])
  

leng = 0
for w in words:
  s = 0
  for c in w:
    s += alfa.index(c)
  if isTriangular(s): leng += 1

  print(leng)
