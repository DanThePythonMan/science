def percentYield():
  max=float(input("Max: "))
  real=float(input("Real: "))
  total= 100 * real
  total = total / max
  print(f"%Yield = {total}")