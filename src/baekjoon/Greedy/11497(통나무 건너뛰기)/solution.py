t = int(input())

for _ in range(t):
  n = int(input())
  mylist = list(map(int, input().split()))

  mylist.sort(reverse=True)
  mymax = 0

  for i in range(n-2):
    if mymax < mylist[i]-mylist[i+2]:
      mymax = mylist[i]-mylist[i+2]

  print(mymax)
