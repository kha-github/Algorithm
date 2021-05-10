from collections import deque

def fun(start, target):
  myq = deque([start, ])
  mycnt = deque([1, ])

  while myq:

    val = myq.popleft()
    cnt = mycnt.popleft() 


    if val*10 + 1 < target:
      myq.append(val*10+1)
      mycnt.append(cnt+1)
    if val*2 < target:
      myq.append(val*2)
      mycnt.append(cnt+1)
    if val*10 + 1 == target or val*2 == target:
      return cnt+1

    cnt += 1

  return -1


a, b = map(int, input().split())
if a == b:
  print(0)
else:
  print(fun(a, b))
