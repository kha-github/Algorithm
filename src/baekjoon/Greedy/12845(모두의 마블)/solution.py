n = int(input())
mylist = list(map(int, input().split()))

mylist.sort()
cnt = 0
for i in range(len(mylist)):
  if i != len(mylist)-1:
    cnt += mylist[i]
  else:
    cnt += mylist[i] * (n-1)

print(cnt)
