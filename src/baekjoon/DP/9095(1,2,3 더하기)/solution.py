def funct(n):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif dptable[n] > 0:
    return dptable[n]
  
  dptable[n] = funct(n-1) + funct(n-2) + funct(n-3)

  return dptable[n]


t = int(input())

for _ in range(t):
  n = int(input())
  dptable = [0]*(n+1)
  print(funct(n))
