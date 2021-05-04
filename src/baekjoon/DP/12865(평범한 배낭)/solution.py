n, k = map(int, input().split())

w = []
v = []
dptable = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
  w_temp, v_temp = map(int, input().split())
  w.append(w_temp)
  v.append(v_temp)

for i in range(1, n+1):
  for j in range(1, k+1):
    if i == 0 or j == 0:
      continue
    if w[i-1] <= j:
      dptable[i][j] = max(dptable[i-1][j-w[i-1]]+v[i-1], dptable[i-1][j])
    else:
      dptable[i][j] = dptable[i-1][j]

print(dptable[n][k])
