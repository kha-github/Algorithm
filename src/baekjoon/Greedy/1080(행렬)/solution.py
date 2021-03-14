def flip(a, b):
  global mylist

  for k in range(3):
    for j in range(3):
      mylist[a+k][b+j] = '1' if mylist[a+k][b+j]=='0' else '0'
 
  return mylist

m, n = map(int, input().split())

mylist = []
targetlist = []

for i in range(m):
  temp = list(input())
  mylist.append(temp)

for i in range(m):
  temp = list(input())
  targetlist.append(temp)

cnt = 0

for k in range(m-2):
  for j in range(n-2):
    if mylist[k][j] != targetlist[k][j]:
      mylist = flip(k, j)
      cnt += 1
  


for k in range(m):
  for j in range(n):
    if mylist[k][j] != targetlist[k][j]:
      cnt = -1
      break

print(cnt)
