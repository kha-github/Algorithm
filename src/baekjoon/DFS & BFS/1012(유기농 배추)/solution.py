import collections

def BFS(a, b):

  global m
  global n 
  global line
  global visit

  move_x = [0, 0, 1, -1]
  move_y = [1, -1, 0, 0]

  myq = collections.deque()
  myq.appendleft((a, b))

  while(True):
    if len(myq) == 0:
      return

    cur = myq.pop()

    for i in range(4):
      next_x = cur[0] + move_x[i]
      next_y = cur[1] + move_y[i]

      if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
        if line[next_x][next_y] == 1 and visit[next_x][next_y] == 0:
          myq.appendleft((next_x, next_y))
          line[next_x][next_y] = 0

t = int(input())

for i in range(t):
  m, n, k = map(int, input().split())

  line = [[0]*n for _ in range(m)]
  visit = [[0]*n for _ in range(m)]

  cnt = 0

  for i in range(k):
    a, b = map(int, input().split())
    line[a][b] = 1

  for i in range(m):
    for j in range(n):
      if line[i][j] == 1:
        BFS(i, j)
        cnt += 1

  print(cnt)

