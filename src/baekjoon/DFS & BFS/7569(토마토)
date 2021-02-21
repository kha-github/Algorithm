import collections

def isNone():
  global mylist
  global h, m, n

  for j in range(h):
    for k in range(n):
      for i in range(m):
        if mylist[j][k][i] == 0:
          return 0
  
  return 1


def BFS(arglist):
  
  global h, m, n
  global mylist

  myq = collections.deque()
  
  cnt = 0

  move_m = [0, 0, 1, -1, 0, 0]
  move_n = [1, -1, 0, 0, 0, 0]
  move_h = [0, 0, 0, 0, 1, -1]

  for item in arglist:
    myq.appendleft(item)
    
  while(True):

    if len(myq) == 0:
      if isNone() == 0:
        return -1
      else:
        return cnt-1
      
    temp = len(myq)

    cnt += 1

    for _ in range(temp):

      cur = myq.pop()

      for i in range(6):
        cur_h = cur[0] + move_h[i]
        cur_n = cur[1] + move_n[i]
        cur_m = cur[2] + move_m[i]
        if cur_n >= 0 and cur_h >= 0 and cur_m >= 0 and cur_n < n and cur_m < m and cur_h < h and  mylist[cur_h][cur_n][cur_m] == 0:
            myq.appendleft((cur_h, cur_n, cur_m))
            mylist[cur_h][cur_n][cur_m] = 1
    


m, n, h = map(int, input().split())

mylist = []
one_list = []

for j in range(h):
  templist = []
  for i in range(n):
    templist.append(list(map(int, input().split())))  
  mylist.append(templist)


for j in range(h):
  for i in range(n):
    for k in range(m):
      if mylist[j][i][k] == 1:
        one_list.append((j, i, k))


print(BFS(one_list))
