import heapq

n = int(input())
mylist = []
for _ in range(n):
  heapq.heappush(mylist, int(input()))
if n == 1:
  print(0)
  exit(0)

mylist.sort()

result = 0

while(len(mylist) != 1):
  arg1 = heapq.heappop(mylist)
  arg2 = heapq.heappop(mylist)
  heapq.heappush(mylist, arg1+arg2)
  result += arg1+arg2

print(result)
