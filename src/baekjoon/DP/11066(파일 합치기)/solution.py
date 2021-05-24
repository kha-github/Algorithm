t = int(input())

for _ in range(t):
  n = int(input())
  mylist = list(map(int, input().split()))
  sum = [0, ]
  dp =[[0]*n for _ in range(n)] 
    
  for i in range(n):
    sum.append(sum[-1]+mylist[i])

  for i in range(1, n):
    for j in range(0, n-i):
      if i == 1:
        dp[j][j+i] = mylist[j] + mylist[j+1]
      else: 
        dp[j][j+i] = 10**10
        for k in range(j, j+i):
          dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + sum[j+i+1]-sum[j])

                  
      
  print(dp[0][-1])
