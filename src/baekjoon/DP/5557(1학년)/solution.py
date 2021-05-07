n = int(input())
mylist = list(map(int, input().split()))
dptable = [[0]*21 for _ in range(n)]
dptable[0][mylist[0]] = 1

for i in range(1, n-1):
  for k in range(0, 21):
    if dptable[i-1][k] != 0:
      if k + mylist[i] <= 20:
        dptable[i][k + mylist[i]] += dptable[i-1][k]
      if k - mylist[i] >= 0:
        dptable[i][k - mylist[i]] += dptable[i-1][k]

print(dptable[-2][mylist[-1]])
    
