n = int(input())
mylist = list(map(int, input().split()))

mylist.sort()

cnt = 0

for i in mylist:
  cnt += i*n
  n -= 1

print(cnt)
