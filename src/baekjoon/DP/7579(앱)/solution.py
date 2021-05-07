n, k = map(int, input().split())

w = list(map(int, input().split()))
v = list(map(int, input().split()))

dptable = [[0]*(sum(v)+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, sum(v)+1):
    if i == 0 or j == 0:
      continue
    if j - v[i-1] >= 0:
      dptable[i][j] = max(dptable[i-1][j-v[i-1]]+w[i-1], dptable[i-1][j])
    else:
      dptable[i][j] = dptable[i-1][j]

for idx in range(len(dptable[-1])):
  if dptable[-1][idx] >= k:
    print(idx)
    break
    
