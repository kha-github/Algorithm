import collections

def BFS(y, x):
  global mylist
  global w, h

  move_x = [0, 0, 1, -1, 1, -1, 1, -1]
  move_y = [1, -1, 0, 0, -1, 1, 1, -1]

  myq = collections.deque()
  myq.appendleft((x, y))

  while(True):
    if len(myq) == 0:
      break

    cur = myq.pop()

    for i in range(8):
      cur_x = cur[0] + move_x[i]
      cur_y = cur[1] + move_y[i]

      if cur_x >= 0 and cur_y >= 0 and cur_x < w and cur_y < h:
        if mylist[cur_y][cur_x] == 1:
          myq.appendleft((cur_x, cur_y))
          mylist[cur_y][cur_x] = 0


      

while(True):
  w, h = map(int, input().split())
  if w==0 and h==0:
    break

  mylist = []

  for i in range (h):
    mylist.append(list(map(int, input().split())))  

  cnt = 0

  for m in range(h):
    for n in range(w):
      if mylist[m][n] == 1:
        BFS(m, n)
        cnt += 1

  print(cnt)
