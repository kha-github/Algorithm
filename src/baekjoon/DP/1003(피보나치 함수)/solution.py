t = int(input())

for _ in range(t):
  n = int(input())

  one = [0, 1, 1]
  zero = [1, 0, 1]

  for i in range(3, n+1, 1):
    one.append(one[i-2]+one[i-1])
    zero.append(zero[i-2]+zero[i-1])

  print(zero[n], one[n])
