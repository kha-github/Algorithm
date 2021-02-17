import copy
from itertools import combinations
import itertools

def Function(mylist, _combi_steplist_2d):

  global n, m

  sum_cnt = 0

  _mylist = copy.deepcopy(mylist)
  for i in range(3):   
    _mylist[_combi_steplist_2d[i][0]][_combi_steplist_2d[i][1]] = 1

  for row in range(n):
    for col in range(m):
      if _mylist[row][col] == 2:
        sum_cnt += DFS(_mylist, row, col)

  return sum_cnt
  

def DFS(_mylist, a, b):

  global n, m

  das = (0, 1, 0, -1)
  dbs = (1, 0, -1, 0)

  cnt = 1

  _mylist[a][b] = 1

  stack = [(a, b)]

  while(stack):
    a, b = stack.pop()
    for da, db in zip(das, dbs):
      na, nb = a + da, b + db
      
      if na >= 0 and na < n and nb >= 0 and nb < m and _mylist[na][nb] == 0:

        stack.append((na, nb))
        _mylist[na][nb] = 1
        cnt += 1

  return cnt

n, m = map(int, input().split())

mylist = []
steplist = []
combi_steplist = []
one_cnt = 0

for i in range(n):
  mylist.append(list(map(int, input().split())))

for row in range(n):
  for col in range(m):
    if mylist[row][col] == 0:
      steplist.append((row, col))
    elif mylist[row][col] == 1:
      one_cnt += 1

for i in combinations(steplist, 3):
  combi_steplist.append(i)

min_list = []

for i in range (len(combi_steplist)):
  min_list.append(Function(mylist, combi_steplist[i]))

min_list.sort()

print(m*n - one_cnt -3-min_list[0])

