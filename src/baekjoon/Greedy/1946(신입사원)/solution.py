t = int(input())
for _ in range(t):
  n = int(input())
  mylist=[]
  for _ in range(n):
    mylist.append(list(map(int, input().split())))

  mylist.sort(key=lambda x:x[0])

  mylist = list(zip(*mylist))[1]
  mymin = mylist[0]

  for i in range(1, n):
    if mylist[i] > mymin:
      n -= 1
    else:
      mymin = mylist[i]
  
  print(n)
