import collections

def BFS(x, y):

  move_x = [0, 0, 1, -1]
  move_y = [1, -1, 0, 0]

  myq = collections.deque()
  myq.appendleft((x, y))
  visit[x][y] = 1 

  while(True):
    if len(myq) == 0:
      break

    cur = myq.pop()

    for i in range(4):
      cur_x = cur[0] + move_x[i]
      cur_y = cur[1] + move_y[i]

      if cur_x >= 0 and cur_y >= 0 and cur_x < n and cur_y < n:
        if mylist[cur_x][cur_y] != -1 and visit[cur_x][cur_y] == 0:
          myq.appendleft((cur_x, cur_y))
          visit[cur_x][cur_y] = 1 

n = int(input())
mylist = []
mycnt = [1, ]

for i in range(n):
  temp = list(map(int, input().split()))
  mylist.append(temp)

max_h = max(map(max, mylist))

for k in range(max_h+1):
  for a in range(n):
    for b in range(n):
      if mylist[a][b] <= k+1:
        mylist[a][b] = -1

  cnt = 0
  visit = [[0] * n for _ in range(n)]

  for a in range(n):
    for b in range(n):
      if mylist[a][b] != -1 and visit[a][b] != 1:
        BFS(a, b)
        cnt += 1

  if cnt == 0:
    break

  mycnt.append(cnt)

print(max(mycnt))
