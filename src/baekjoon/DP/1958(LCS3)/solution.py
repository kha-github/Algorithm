X = input()
Y = input()
Z = input()

arr = [[[0 for _ in range(max(len(X), len(Y), len(Z))+1)] for _ in range(max(len(X), len(Y), len(Z))+1)] for _ in range(max(len(X), len(Y), len(Z))+1)]


for i in range(1, len(X)+1):
  for k in range(1, len(Y)+1):
    for j in range(1, len(Z)+1):
      if (X[i-1] == Y[k-1] and Y[k-1] == Z[j-1]):
        arr[i][k][j] = arr[i-1][k-1][j-1] + 1;
      else:
        arr[i][k][j] = max(arr[i-1][k][j], arr[i][k-1][j], arr[i][k][j-1])

print(arr[len(X)][len(Y)][len(Z)])
