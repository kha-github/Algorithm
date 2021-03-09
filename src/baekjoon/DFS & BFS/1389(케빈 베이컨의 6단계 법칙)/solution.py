import collections

def BFS(x):
  global n

  myq = collections.deque()
  myq.appendleft(x)

  myvisit = [0]*n
  myvisit[x] = 1

  while(myq):
    cur = myq.pop()
    
    for i in range (n):
      if cur == i or x == i:
        continue
      if mylist[cur][i] == 1 and myvisit[i] == 0:
        myq.appendleft(i)
        myvisit[i] = 1
        mylist[x][i] = mylist[x][cur]+1
        mylist[i][x] = mylist[x][cur]+1


n, m = map(int, input().split())

mylist = [[0]*n for _ in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  mylist[a-1][b-1] = 1
  mylist[b-1][a-1] = 1

for i in range(n):
  BFS(i)

result = 0
mysum = 99

for i in range(n):
  if mysum > sum(mylist[i]):
    result = i
    mysum = sum(mylist[i])

print(result+1)
