import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  mylist = list(map(int, sys.stdin.readline().split()))
  result = 0
  mymax = mylist[-1]

  for i in range(len(mylist)-2, -1, -1):
    if mylist[i] > mymax:
      mymax = mylist[i]
    else:
      result += mymax - mylist[i]

  print(result)

