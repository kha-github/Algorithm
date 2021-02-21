import collections

def BFS(arglist):
  
  global m, n
  global mylist

  myq = collections.deque()
  
  cnt = 0
  target_cnt = len(arglist)
  next_target_cnt = 0

  move_m = [0, 0, 1, -1]
  move_n = [1, -1, 0, 0]

  for item in arglist:
    myq.appendleft(item)
    

  while(True):

    if len(myq) == 0:
      if 0 in sum(mylist, []):
        return -1
      else:
        return cnt

    target_cnt -= 1
    
    cur = myq.pop()

    for i in range(4):
      cur_n = cur[0] + move_n[i]
      cur_m = cur[1] + move_m[i]
      if cur_n >= 0 and cur_m >= 0 and cur_n < n and cur_m < m:
        if mylist[cur_n][cur_m] == 0:
          next_target_cnt += 1
          myq.appendleft((cur_n, cur_m))
          mylist[cur_n][cur_m] = 1

    if target_cnt == 0 and len(myq) != 0:
      cnt +=1 
      target_cnt = next_target_cnt
      next_target_cnt = 0


m, n = map(int, input().split())

mylist = []
one_list = []

for i in range(n):
  mylist.append(list(map(int, input().split())))  
  for k in range(m):
    if mylist[i][k] == 1:
      one_list.append((i, k))


print(BFS(one_list))
