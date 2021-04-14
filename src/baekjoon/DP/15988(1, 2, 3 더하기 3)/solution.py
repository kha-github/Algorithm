def funct(n):
  for i in range(4, n+1, 1):
    if dptable[i] == 0:
      dptable[i] = (dptable[i-1] + dptable[i-2] + dptable[i-3])%1000000009
  return dptable[n]

t = int(input())

for _ in range(t):
  n = int(input())
  dptable = [0]*(n+3)
  dptable[1] = 1
  dptable[2] = 2
  dptable[3] = 4
  print(funct(n)%1000000009)
