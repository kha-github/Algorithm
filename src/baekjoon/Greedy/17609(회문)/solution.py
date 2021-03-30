def function(check, a, b):
  result = 0

  while True:
    if result == 2 or a >= b:
      break
    if mylist[i][a] == mylist[i][b]:
      a += 1
      b -= 1
    elif check == 0 and mylist[i][a] == mylist[i][b-1]:
      a += 1
      b -= 2
      result += 1
    elif check == 1 and mylist[i][a+1] == mylist[i][b]:
      a += 2
      b -= 1
      result += 1
    else:
      result = 2
      break

  return result

n = int(input())
mylist = []

for _ in range(n):
  mylist.append(input())

for i in range(n):
  result = 0
  another_result = 0
  result = function(0, 0, len(mylist[i])-1)
  if result == 2:
    another_result = function(1, 0, len(mylist[i])-1)
    result = min(result, another_result)
  print(result)
    
