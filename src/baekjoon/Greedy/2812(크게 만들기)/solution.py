n, k = map(int, input().split())
value = input()

result = []

for i in range(n):
  while k != 0 and len(result) != 0 and result[-1] < value[i]:
    if result[-1] < value[i]:
      del result[-1]
      k -= 1
  result.append(value[i])

print(''.join(result[:len(result)-k]))
