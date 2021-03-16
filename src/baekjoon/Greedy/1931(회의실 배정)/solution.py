k = int(input())

mylist= []

for i in range(k):
  mylist.append(list(map(int, input().split())))

mylist = sorted(mylist ,key = lambda x: x[0])
mylist = sorted(mylist ,key = lambda x: x[1])

cnt = 1
end = mylist[0][1]

for i in range(1, k):
  if end <= mylist[i][0]:
    end = mylist[i][1]
    cnt += 1

print(cnt)
