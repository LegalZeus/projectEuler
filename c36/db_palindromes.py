def toBinary(n):
  r =""

  while n >=1:
    if n%2 == 0: r += "0"
    else: r += "1"

    n = int(n/2)
  return "".join(reversed(r))



def isPalindrom(s) -> bool:
  if s == "".join(reversed(s)):
    return True
  else:
    return False

sum = 0
for n in range(1, 1000000):
  if isPalindrom(str(n)) and isPalindrom(toBinary(n)):
    sum += n
    print(sum)


print(f"\n\nsum : {sum} \n\n")

