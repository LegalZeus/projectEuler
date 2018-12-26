with open("grid.txt", "r") as f:
  numbers = [int(n) for n in f.read().split("\n") if n != ""]

s = sum(numbers)

print(f"solution : {str(s)[:10]}") 





