from math import ceil, floor, sqrt

def grid(length):
  x = ceil(sqrt(length))
  y = round(sqrt(length))
  return x, y

for i in range(0, 101):
  x, y = grid(i)
  print("nb :", i, "values", x, y)