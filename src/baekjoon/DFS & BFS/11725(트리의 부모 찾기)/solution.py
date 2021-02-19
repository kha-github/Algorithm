import sys
sys.setrecursionlimit(1000000)

def DFS(start):
  global n
  global mylist
  global visit
  global result

  visit[start-1] = 1

  for i in range(len(mylist[start-1])):
    next = mylist[start-1][i]

    if visit[next-1] != 1:
      result[next-1] = start
      DFS(next)
  

n = int(input())

mylist = [[] for _ in range (n)]
visit = [0]*n
result = [0]*n

for i in range(n-1):
  temp = tuple(map(int, input().split()))
  mylist[temp[0]-1].append(temp[1])
  mylist[temp[1]-1].append(temp[0])


DFS(1)

for i in range(1, len(result)):
  print(result[i])
