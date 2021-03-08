import collections

def BFS(x, y, list, visit, part):
  global n

  move_x = [0, 0, 1, -1]
  move_y = [1, -1, 0, 0]

  myq = collections.deque()
  myq.appendleft((x, y))
  visit[x][y] = 0

  if (part == 1):
    while(myq):
      cur = myq.pop()

      for i in range(4):
        cur_x = cur[0] + move_x[i]
        cur_y = cur[1] + move_y[i]
        

        if cur_x >= 0 and cur_y >= 0 and cur_x < n and cur_y < n:
          
          if (list[cur[0]][cur[1]] == list[cur_x][cur_y]) or (list[cur[0]][cur[1]] == 'R' and list[cur_x][cur_y] == 'G') or (list[cur[0]][cur[1]] == 'G' and list[cur_x][cur_y] == 'R'):
            if visit[cur_x][cur_y] != 1:
              myq.appendleft((cur_x, cur_y))
              visit[cur_x][cur_y] = 1  

  if (part == 0):
    while(myq):
      cur = myq.pop()

      for i in range(4):
        cur_x = cur[0] + move_x[i]
        cur_y = cur[1] + move_y[i]
        

        if cur_x >= 0 and cur_y >= 0 and cur_x < n and cur_y < n:
          
          if (list[cur[0]][cur[1]] == list[cur_x][cur_y]):
            if visit[cur_x][cur_y] != 1:
              myq.appendleft((cur_x, cur_y))
              visit[cur_x][cur_y] = 1  




n = int(input())
mylist = []
copylist = []
myvisit = [[0]*n for _ in range(n)]
copyvisit = [[0]*n for _ in range(n)]

normal = 0
abnormal = 0

for i in range(n):
  temp = list(input())
  mylist.append(temp)
  copylist.append(temp)

for k in range(n):
  for j in range(n):
    if myvisit[k][j] != 1:
      BFS(k, j, mylist, myvisit, 0)
      normal += 1

print(normal)

for k in range(n):
  for j in range(n):
    if copyvisit[k][j] != 1:
      BFS(k, j, copylist, copyvisit, 1)
      abnormal += 1

print(abnormal)
