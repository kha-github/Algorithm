'''
첫째줄에 list index의 개수, 더해야 하는 횟수, 한 index를 연속해서 더할 수 있는 횟수를 차례대로 입력받고
두번째줄에서 list의 값들을 입력받는다
list의 idnex를 정해진 횟수만큼 더햇을 때에 나올 수 있는 최대 값을 구하는 문제
단 index를 더할 때 연속으로 더할 수 있는 횟수가 정해져 있음을 주의
'''
n, m, k = map(int, input().split())
mylist = list(map(int, input().split()))

mylist.sort(reverse=True)

current_k = 0
sum = 0

for cnt in range(m):
  if current_k == k:
    current_k = 0
    sum += mylist[1]
    continue

  sum += mylist[0]
  current_k += 1
  
print(sum)
