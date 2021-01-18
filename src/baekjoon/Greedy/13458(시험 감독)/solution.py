import math

n = int(input())
mylist = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0

for i in range(len(mylist)):
  if mylist[i] < b :
    mylist[i] = 0
  else :
    mylist[i] = mylist[i] - b
  cnt += 1

for i in mylist:
  cnt += math.ceil(float(i) / float(c))

print(cnt)
