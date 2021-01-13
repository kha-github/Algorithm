n, k = map(int, input().split())

mylist = []
cnt = 0

for i in range(n):
  mylist.append(int(input()))

while k!=0:
  n -= 1
  if k < mylist[n]:
    continue;

  cnt += k//mylist[n]
  k %= mylist[n]

print(cnt)
