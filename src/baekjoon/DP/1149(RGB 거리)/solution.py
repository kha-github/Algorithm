n = int(input())
dptable = []

for _ in range(n):
  dptable.append(list(map(int, input().split())))

for i in range(1, n, 1):
  dptable[i][0] = min(dptable[i-1][1], dptable[i-1][2]) + dptable[i][0]
  dptable[i][1] = min(dptable[i-1][0], dptable[i-1][2]) + dptable[i][1]
  dptable[i][2] = min(dptable[i-1][0], dptable[i-1][1]) + dptable[i][2]
print(min(dptable[n-1]))
