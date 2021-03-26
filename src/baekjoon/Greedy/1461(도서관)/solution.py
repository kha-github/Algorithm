n, m = map(int, input().split())
mylist = list(map(int, input().split()))
poslist = []
neglist = []

mylist.append(0)
mylist.sort()

neglist = mylist[:mylist.index(0)]
poslist = mylist[mylist.index(0)+1:]

poslist.sort(reverse=True)

step = 0

for i in range(0, len(neglist), m):
  step += abs(neglist[i])*2

for i in range(0, len(poslist), m):
  step += abs(poslist[i])*2

if len(neglist)!=0 and len(poslist)!=0:
  print(step - max(abs(min(neglist)), max(poslist)))
elif len(neglist)!=0:
  print(step - abs(min(neglist)))
else:
  print(step - abs(max(poslist)))
