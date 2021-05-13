n = int(input())
mylist = []
for _ in range(n):
  a, b = map(int, input().split())
  mylist.append((a, b))

cnt = [1]*n

for idx in range(n):
  for k in range(n):
    if k == idx:
      continue
    if mylist[idx][0] < mylist[k][0] and mylist[idx][1] < mylist[k][1]:
      cnt[idx] += 1

for i in range(n):
  print(cnt[i], end=" ")
