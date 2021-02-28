import collections

def BFS(start, target):
  myq = collections.deque()
  myq.appendleft(start)

  step = 0

  visit = [0]*100001
  
  while(True):
    cur_qlen = len(myq)
    
    step += 1

    for _ in range(cur_qlen):
      cur = myq.pop()
      move_cur = [-1, 1, cur]

      for i in range(3):
        next = cur + move_cur[i]
        

        if (next >= 0 and next <= 100000 and visit[next] == 0):  
          if next == target:
            return step
          
          visit[next] = 1
          myq.appendleft(next)
        

n, k = map(int, input().split())

if n==k:
  print(0)
else:
  print(BFS(n, k))
