def funct(n):
  if n == 0:
    return 1
  if n < 0:
    return 0
  if dptable[n] > 0:
    return dptable[n]
  
  dptable[n] = funct(n-1)%10007 + funct(n-2)%10007

  return dptable[n]

n = int(input())

dptable = [0]*(n+1)

print(funct(n)%10007)

