from collections import deque

n, k = map(int, input().split())

mylist = deque([])
result = []

for i in range(n):
  mylist.append(i+1)

while (len(mylist)!=0):
  for i in range(k-1):
    mylist.append(mylist.popleft())
  result.append(mylist.popleft())

print("<%s>" %(", ".join(map(str, result))))
