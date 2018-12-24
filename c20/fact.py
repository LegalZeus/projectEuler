


def factorial(n):
  r = 1
  while n >= 1:
    r *= n
    n -= 1

  return r


def digits_sum(n):
  s = str(n)
  r = 0
  for x in s:
    r += int(x)

  return r


o = factorial(100)
print(digits_sum(o))
