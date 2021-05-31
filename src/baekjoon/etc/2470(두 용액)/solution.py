n = int(input())
mylist = list(map(int, input().split()))

mylist.sort()

right = len(mylist)-1
left = 0

result = [left, right, mylist[left]+mylist[right]]

while left<right:

  if mylist[left]+mylist[right] < 0:
    left = left+1
  elif mylist[left]+mylist[right] > 0:
    right = right-1
  else:
    print(mylist[left], mylist[right])
    exit(0)
  
  if left == right:
    break

  if abs(result[2]) > abs(mylist[left]+mylist[right]):
    result = []
    result.append(left)
    result.append(right)
    result.append(mylist[left]+mylist[right])

print(mylist[result[0]], mylist[result[1]])
