import sys

n = int(input())
c_weight = list(map(int, sys.stdin.readline().split()))
m = int(input())
b_weight = list(map(int, sys.stdin.readline().split()))

c_weight.sort(reverse=True)
b_weight.sort(reverse=True)

if b_weight[0] > c_weight[0]:
  print(-1)
else:
  cnt = 0

  while len(b_weight) != 0:
    cnt += 1
    cur_loc = 0
    for cur_c in c_weight:
      for cur_b_idx in range(cur_loc, len(b_weight)):
        if b_weight[cur_b_idx] <= cur_c:
          del b_weight[cur_b_idx]
          cur_loc = cur_b_idx
          break
      if len(b_weight) == 0:
        break

  print(cnt)
