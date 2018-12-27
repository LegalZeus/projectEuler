p = "123456789"

sum = 0
results = []
for a in range(1, 10000):
  for b in range(1, 10000):
    if sorted(str(a)+str(b)+str(a*b)) == sorted(p) and not str(a*b) in results:
      print(a, b, "\n")
      sum += a*b
      results.append(str(a*b))
      print(f"\n\nsum : {sum}\n\n")

print(f"\n\nsum : {sum}\n\n")
