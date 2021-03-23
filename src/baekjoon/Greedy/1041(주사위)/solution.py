n = int(input())
dice = list(map(int, input().split()))

if n == 1:
  dice.sort()
  print(sum(dice[0:5]))
  exit(0)
  
case1 = min(dice)
case2 = min(dice[0]+dice[1],dice[0]+dice[2],dice[0]+dice[3],dice[0]+dice[4],dice[1]+dice[2],dice[1]+dice[3],dice[1]+dice[5],dice[2]+dice[4],dice[2]+dice[5],dice[3]+dice[4],dice[3]+dice[5],dice[4]+dice[5])
case3 = min(dice[0]+dice[1]+dice[2], dice[0]+dice[2]+dice[4], dice[0]+dice[3]+dice[4], dice[0]+dice[1]+dice[3], dice[5]+dice[1]+dice[2], dice[5]+dice[2]+dice[4], dice[5]+dice[3]+dice[4], dice[5]+dice[1]+dice[3])

numcase1 = (n-2)*(n-2) + (n-2)*(n-1)*4
numcase2 = (n-2)*4+(n-1)*4
numcase3 = 4

print(numcase1*case1 + numcase2*case2 + numcase3*case3)
