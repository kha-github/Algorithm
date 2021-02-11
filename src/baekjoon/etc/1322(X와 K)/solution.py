X, Z = map(int, input().split())
Y = 9223372036854775807^X

cnt = 0

Y = list(bin(Y))
Z = list(bin(Z))
result = ['0','b']

temp = len(Z)-1

for k in range(len(Y)-1, 0, -1):
  if(Y[k] == "1"):
    result = result[0:2] + Z[temp:temp+1] + result[2:]
    temp -= 1
    if temp == 1:
      break
  else:
    result = result[0:2] + result[0:1] + result[2:]

print(int(''.join(result),2))
