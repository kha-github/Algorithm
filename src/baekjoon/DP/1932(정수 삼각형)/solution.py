n = int(input())
mylist = []

for _ in range(n):
  mylist.append(list(map(int, input().split())))

dptable = [[0]*n for _ in range(n)]
dptable[0][0] = mylist[0][0]

for i in range(1, n, 1):
  for j in range(i+1):
    if j == 0:
      dptable[i][j] = dptable[i-1][0] + mylist[i][j]
    elif j == i:
      dptable[i][j] = dptable[i-1][i-1] + mylist[i][j]
    else:
      dptable[i][j] = max(dptable[i-1][j-1], dptable[i-1][j]) + mylist[i][j]

print(max(dptable[n-1]))
    
