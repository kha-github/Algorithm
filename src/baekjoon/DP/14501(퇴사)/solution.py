n = int(input())

mylist = []
dptable = [0]*(n+1)

for _ in range(n):
  a, b = map(int, input().split())
  mylist.append((a, b))

for idx in range(n):
  if idx+mylist[idx][0]-1 < n:
    mymax = 0
    if idx != 0:
      mymax = max(dptable[:idx])
    dptable[idx+mylist[idx][0]-1] = max(dptable[idx+mylist[idx][0]-1], mymax + mylist[idx][1])
    
print(max(dptable))
  
