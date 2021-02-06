X = input()
Y = input()

arr = [[0 for _ in range(max(len(X), len(Y))+1)] 
for _ in range(max(len(X), len(Y))+1)]

for i in range(1, len(X)+1):
  for k in range(1, len(Y)+1):
    if (X[i-1] == Y[k-1]):
      arr[i][k] = arr[i-1][k-1] + 1;
    elif (arr[i-1][k] >= arr[i][k-1]):
      arr[i][k] = arr[i-1][k]
    else:
      arr[i][k] = arr[i][k-1]

print(arr[len(X)][len(Y)])
