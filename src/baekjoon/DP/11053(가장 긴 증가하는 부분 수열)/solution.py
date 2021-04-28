n = int(input())
mylist = list(map(int, input().split()))
dptable = [1]*n

for i in range(len(mylist)):
  for j in range(i):
    if mylist[i] > mylist[j]:
      dptable[i] = max(dptable[i], dptable[j]+1)

print(max(dptable))
