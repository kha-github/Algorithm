import collections

def BFS(a, b):

  global line
  global n

  myq = collections.deque()
  myq.appendleft(a)

  visit = [0]*n

  while(True):
    if len(myq) == 0:
      return -1

    cur = myq.pop()

    for i in range(n):
      if line[cur-1][i] == 1 and visit[i] == 0:

        myq.appendleft(i+1)
        line[cur-1][i] = 0
        line[i][cur-1] = 0
        visit[i] = visit[cur-1] + 1

        if i == b-1:
          return visit[i]
  


n = int(input())
target_x, target_y = map(int, input().split())
m = int(input())

line = [[0]*n for _ in range(n)]

for i in range(m):
  x, y = map(int, input().split())
  line[x-1][y-1] = 1
  line[y-1][x-1] = 1

if (target_x == target_y):
  print(0)
else: 
  print(BFS(target_x, target_y))

