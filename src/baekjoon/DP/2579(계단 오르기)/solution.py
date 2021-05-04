n = int(input())
mylist = []
for _ in range(n):
  mylist.append(int(input()))
dptable = [0]*n
dptable[0] = mylist[0]
for i in range(1, 3):
  if i == 1 and n >= 2:
    dptable[1] = mylist[0]+mylist[1]
  if i == 2 and n >= 3:
    dptable[2] = max(mylist[0], mylist[1])+mylist[2]

for i in range(3, n):
  dptable[i] = max(dptable[i-3]+mylist[i-1], dptable[i-2])+mylist[i]

print(dptable[-1])
