n = int(input())

result = 0
mylist = []

for i in range(n):
  mylist.append(int(input()))

mylist.sort()

for i in range(n):
  result = max(result, mylist[i]*(n-i))

print(result)
