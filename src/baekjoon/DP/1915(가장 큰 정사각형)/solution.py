import math

n, m = map(int, input().split())

mylist = []

for i in range(n):
  mylist.append(list(map(int, input())))
  
for i in range(n):
  for k in range(m):
    if i > 0 and k > 0 and mylist[i][k] == 1:
      mylist[i][k] = min(mylist[i][k-1], mylist[i-1][k-1], mylist[i-1][k])+1


print(int(math.pow(max(map(max, mylist)),2)))

