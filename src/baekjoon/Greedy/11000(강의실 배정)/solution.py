import heapq

k = int(input())

myheap = []
mylist= []
for i in range(k):
  mylist.append(list(map(int, input().split())))

mylist = sorted(mylist ,key = lambda x: x[0])

for i in range(k):
  if (len(myheap) != 0 and mylist[i][0] >= myheap[0]):
    heapq.heappop(myheap)
  heapq.heappush(myheap, mylist[i][1])

print(len(myheap))
