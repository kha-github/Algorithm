n, m = map(int, input().split())
mylist = list(map(int, input().split()))

mylist.sort()
min = mylist[0]

for _ in range(m):
  mysum = mylist[0] + mylist[1]
  mylist[0] = mysum
  mylist[1] = mysum

  mylist.sort()

print(sum(mylist))
