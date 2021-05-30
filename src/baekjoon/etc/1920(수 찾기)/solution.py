def fun(targetItem, start, end):
  global mylist

  if start > end:
    return 0
  m = int((start+end)/2)
  if targetItem == mylist[m]:
    return 1
  elif targetItem < mylist[m]:
    return fun(targetItem, start, m-1)
  else:
    return fun(targetItem, m+1, end)

n = int(input())
mylist = sorted(list(map(int, input().split())))
m = int(input())
targetlist = list(map(int, input().split()))

for item in targetlist:
  print(fun(item, 0, len(mylist)-1))
