import sys
sys.setrecursionlimit(100000000)

def DFS(val):
  global cnt

  if visit[val] == 1:
    return
  visit[val] = 1
  connect = mylist[val]
  cycle.append(val)

  if visit[connect] == 1:
    if connect in cycle:
      cnt += 1
    return
  else:
    DFS(connect)


t = int(input())

for _ in range(t):
  n = int(input())
  mylist = [0]
  cnt = 0

  temp = list(map(int, input().split()))
  for item in temp:
    mylist.append(item)
      
  visit = [0]*(n+1)

  for idx in range(1, n+1):
    if visit[idx] == 0:
      cycle = []
      DFS(idx)
  
  print(cnt)

