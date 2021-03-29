a, b = map(int, input().split())

cnt = 0
while True:
  if b < a:
    cnt = -1
    break
  if b == a:
    cnt += 1
    break
  if b%10 == 1:
    b = int(b/10)
  elif b%2 == 0:
    b = int(b/2)
  else:
    cnt = -1
    break
  cnt += 1
  
print(cnt)
