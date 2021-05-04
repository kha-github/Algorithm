n = int(input())

dptable = [0]*16
dptable[1] = 3

if n%2 == 1:
  print(0)
  exit(0)
for i in range(2, int(n/2)+1):
  dptable[i] = dptable[i-1]*3 + 2 + sum(dptable[:i-1])*2

print(dptable[int(n/2)])
