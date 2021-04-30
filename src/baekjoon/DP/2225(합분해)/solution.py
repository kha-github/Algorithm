n, k = map(int, input().split())

dptable = [[1]*(n+1) for _ in range(k+1)]
result = 1

for i in range(2, k+1):
  for j in range(n+1):
    for h in range(j+1):
      result = dptable[i][j]
      dptable[i][j] = (dptable[i][j]+dptable[i-1][h])%1000000000

print(result)
