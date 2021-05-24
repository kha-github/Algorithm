n = int(input())
mylist = []
for _ in range(n):
  mylist.append(list(map(int, input().split())))
dp =[[0]*n for _ in range(n)] 

for i in range(1, n):
  for j in range(0, n-i):
    if i == 1:
      dp[j][j+i] = mylist[j][0] * mylist[j][1] * mylist[j+i][1]
    else: 
      dp[j][j+i] = 10**10
      for k in range(j, j+i):
        dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + mylist[j][0] * mylist[k][1] * mylist[j+i][1])
                
    
print(dp[0][n-1])
