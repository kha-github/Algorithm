import collections

def BFS(node):

  global n
  global visit
  global mylist
  global count

  myq = collections.deque()
  myq.appendleft(node)
  visit[node] = 1

  while(True):

    if len(myq) == 0:
      return
    
    curnode = myq.pop()

    for i in range(n):
      if visit[i] == 0 and mylist[curnode][i] == 1:  
        myq.appendleft(i)
        count += 1
        mylist[i][curnode] = 0
        mylist[curnode][i] = 0
        visit[i] = 1
    

n = int(input())
pair = int(input())
count = 0

mylist = [[0]*n for _ in range(n)]

visit = [0]*n

for i in range(pair):
  x, y = map(int, input().split())
  mylist[x-1][y-1] = 1
  mylist[y-1][x-1] = 1

BFS(0)

print(count)

