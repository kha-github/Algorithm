import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
  global cnt

  if x < 0 or y < 0 or x == m or y == n or value[x][y] == 1:
    return
  else:
    cnt += 1
    value[x][y] = 1

  dfs(x+1, y)
  dfs(x-1, y)
  dfs(x, y+1)
  dfs(x, y-1)

cnt = 0
result = []

n, m, k = map(int, input().split())
value = [[0]*n for _ in range(m)]


for i in range(k):
  point = list(map(int, input().split()))
  for col in range(point[0], point[2]):
    for row in range(point[1], point[3]):
      value[col][row] = 1

for col in range(m):
  for row in range(n):
    if value[col][row] == 0:
      cnt = 0
      dfs(col, row)
      result.append(cnt)

result.sort()
print(len(result))

for i in result:
  print(i, end = (" "))
