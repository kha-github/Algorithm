import collections

def BFS():
  move_x = [0, 0, 1, -1]
  move_y = [1, -1, 0, 0]
  global deq
  deq = collections.deque()
  deq.appendleft((0, 0))
  global n, m, visit, mylist
  visit[0][0] = 1
  distance[0][0] = 1


  while (True):
    cur = deq.pop()

    for i in range (4):
      next_x = cur[0]+move_x[i]
      next_y = cur[1]+move_y[i]
      if next_x >= 0 and next_y >= 0 and next_x < n and next_y < m and mylist[next_x][next_y] == "1":
        if visit[next_x][next_y] == 0:
          distance[next_x][next_y] = distance[cur[0]][cur[1]]+1
          deq.appendleft((next_x, next_y))
          visit[next_x][next_y] = 1
          if next_x == n-1 and next_y == m-1:
            return distance[next_x][next_y]


n, m = map(int, input().split())
visit = [[0]*m for _ in range(n)]
distance = [[0]*m for _ in range(n)]

deq = collections.deque()

mylist = []

for i in range(n):
  temp = input();
  mylist.append(list(temp))

print(BFS())




