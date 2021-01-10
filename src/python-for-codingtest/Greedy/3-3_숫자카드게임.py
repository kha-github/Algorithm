'''
n*m의 행렬을 받아, 각 행에서의 가장 작은 수들을 모았을 때, 그 중에서 가장 큰 값을 반환한다
'''
n, m = map(int, input().split())

result = -1

for i in range(n):
  mylist = list(map(int, input().split()))
  mylist.sort()

  result = max(result,mylist[0])

print(result)
