import collections

def BFS(a, b):

  move_x = [0, 0, 1, -1]
  move_y = [1, -1, 0, 0]

  myq = collections.deque()
  myq.appendleft((a, b))
  visit[a][b] = 1
  movecountry = []
  movecountry.append((a, b))
  mysum = mylist[a][b]

  while(True):
    if len(myq) == 0:
      return (movecountry, mysum)

    cur = myq.pop()

    for i in range(4):
      next_x = cur[0] + move_x[i]
      next_y = cur[1] + move_y[i]

      if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
        if abs(mylist[cur[0]][cur[1]] - mylist[next_x][next_y]) <= r and abs(mylist[cur[0]][cur[1]] - mylist[next_x][next_y]) >= l and visit[next_x][next_y] == 0:
          myq.appendleft((next_x, next_y))
          movecountry.append((next_x, next_y))
          visit[next_x][next_y] = 1
          mysum += mylist[next_x][next_y]

cnt = 0

n, l, r = map(int, input().split())

mylist = []

for i in range(n):
  temp = list(map(int, input().split()))
  mylist.append(temp)



con = True

while(con):

  templist = []
  sumvaluelist = []
  visit = [[0]*n for _ in range(n)]
  check = False

  for i in range(n):
    for k in range(n):

      if visit[i][k] == 1:
        continue

      temp, sumvalue = BFS(i, k)

      if len(temp) == 1:
        continue

      check= True
      templist.append(temp)
      sumvaluelist.append(sumvalue)


  for j in range (len(templist)):
    for i2 in range (n):
      for k2 in range (n):
        if (i2, k2) in templist[j]:
          mylist[i2][k2] = int(sumvaluelist[j]/len(templist[j]))
  
  
  cnt += 1
  con = check

print(cnt-1)
