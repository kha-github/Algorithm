'''
입력받은 첫번째 숫자가 1이 될 때까지 -1 을 더하거나, 두번째 숫자로 나눈다
단, 두번째 숫자로 나누는 것은 나머지가 0 일 때만 가능하다
'''

n, k = map(int, input().split())

cnt = 0

while(n != 1):
  if (n % k == 0):
    n = n//k 
  else:
    n = n-1
  cnt += 1

print(cnt)
