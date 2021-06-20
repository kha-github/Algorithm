n, m = map(int, input().split())

mylist = [[] for _ in range(n+1)]
dptable = [1]*(n+1)

for _ in range(m):
  a, b = map(int, input().split())
  mylist[b].append(a)

for i in range(1, len(mylist)):
  for k in range(len(mylist[i])):
    dptable[i] = max(dptable[i], dptable[mylist[i][k]]+1)

print(" ".join(map(str,dptable[1:])))
