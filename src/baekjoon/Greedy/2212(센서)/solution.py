n = int(input())
k = int(input())
mylist = list(map(int, input().split()))
mylist.sort()
intervallist = []

for i in range(len(mylist)-1):
  intervallist.append(mylist[i+1]-mylist[i])

intervallist.sort()
result = 0

for j in range(len(intervallist)-k+1):
  result += intervallist[j]     

print(result)
