import collections

def BFS(start_x, start_y, target_x, target_y):

  global size

  if start_x == target_x and start_y == target_y:
    return 0

  move_x = [2, 2, -2, -2, 1, -1, 1, -1]
  move_y = [1, -1, 1, -1, 2, 2, -2, -2]

  mylist = [[0]*size for _ in range(size)]

  myq = collections.deque()
  myq.appendleft((start_x, start_y))

  while(True):

    if len(myq) == 0:
      return mylist[target_x][target_y]

    cur = myq.pop()


    for i in range(8):
      cur_x = cur[0] + move_x[i]
      cur_y = cur[1] + move_y[i]
      if cur_x >= 0 and cur_y >= 0 and cur_x < size and cur_y < size:
          if mylist[cur_x][cur_y] == 0:
            myq.appendleft((cur_x, cur_y))
            mylist[cur_x][cur_y] = mylist[cur[0]][cur[1]] + 1



n = int(input())

for i in range(n):
  size = int(input())
  start_x, start_y = map(int, input().split())
  target_x, target_y = map(int, input().split())

  print(BFS(start_x, start_y, target_x, target_y))



