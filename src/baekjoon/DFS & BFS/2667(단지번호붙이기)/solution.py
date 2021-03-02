import collections

def BFS(x, y):
  global mylist
  global n

  move_x = [0, 0, 1, -1]
  move_y = [1, -1, 0, 0]

  myq = collections.deque()
  myq.appendleft((x, y))
  mylist[x][y] = '0' 

  bfs_cnt = 0

  while(True):
    if len(myq) == 0:
      return bfs_cnt

    cur = myq.pop()
    bfs_cnt += 1

    for i in range(4):
      cur_x = cur[0] + move_x[i]
      cur_y = cur[1] + move_y[i]

      if cur_x >= 0 and cur_y >= 0 and cur_x < n and cur_y < n:
        if mylist[cur_x][cur_y] == '1':
          myq.appendleft((cur_x, cur_y))
          mylist[cur_x][cur_y] = '0'   


      

n = int(input())

mylist = []

for i in range (n):
  mylist.append(list(input()))

cnt = 0
result = []

for m in range(n):
  for k in range(n):
    if mylist[m][k] == '1':
      result.append(BFS(m, k))
      cnt += 1

result.sort()

print(cnt)
for item in result:
  print(item)
