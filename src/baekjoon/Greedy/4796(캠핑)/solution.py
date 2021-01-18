result = []

while True:

  cnt = 0

  mylist = list(map(int, input().split()))
  if mylist[0] == 0 :
    break

  cnt = mylist[2] // mylist[1]
  cnt = cnt * mylist[0]

  if mylist[2] % mylist[1] < mylist[0]:
    cnt += mylist[2] % mylist[1]
  else:
    cnt += mylist[0]

  result.append(cnt)

for i in range(len(result)):
  print("Case " + str(i+1) + ": " + str(result[i]))
