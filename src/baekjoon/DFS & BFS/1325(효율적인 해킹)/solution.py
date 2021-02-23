import sys
input = sys.stdin.readline
import collections

def bfs(node):
  global mylist
  global n
  cnt = 0

  myq = collections.deque()
  myq.append(node)
  visit = [0 for _ in range(n+1)]
  visit[node] = 1

  while(True):
    if len(myq) == 0:
      return cnt

    node = myq.popleft()

    for item in mylist[node]:
      if visit[item] == 0:
        myq.append(item)
        visit[item]=1
        cnt += 1
    

n, m = map(int, input().split())

mylist = [[] for _ in range (n+1)]


result = []
main_maxcnt = 0

for i in range(m):
  a, b = map(int, input().split())
  mylist[b].append(a)


for k in range(1, n+1):
  if len(mylist[k]) != 0:
    return_cnt = bfs(k)
    if main_maxcnt == return_cnt:
      result.append(k)
    elif main_maxcnt < return_cnt:
      result = []
      result.append(k)
      main_maxcnt = return_cnt
    

print(*result)
