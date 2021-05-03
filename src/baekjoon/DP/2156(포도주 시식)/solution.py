n = int(input())
mylist = [0]
dptable = [0 for _ in range(n+1)]

for _ in range(n):
  mylist.append(int(input()))

for i in range(1, n+1):
  if i == 1:
    dptable[1] = mylist[1]
  elif i == 2:
    dptable[2] = dptable[1] + mylist[2]
  else:
    dptable[i] = max(dptable[i-3] + mylist[i-1] + mylist[i], dptable[i-2] + mylist[i], dptable[i-1])  

print(dptable[n])
