n = int(input())

for i in range(n):
  val = i
  temp = i
  while temp!=0:
    val += temp%10
    temp=int(temp/10)

  if val == n:
    print(i)
    exit(0)

print(0)
