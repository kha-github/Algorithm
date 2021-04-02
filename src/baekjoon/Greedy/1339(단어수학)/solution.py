n = int(input())

mylist = []

for _ in range(n):
  mylist.append(input())

cntlist = [0]*26

for item in mylist:
  i = 0
  while item:
    cur = item[-1]
    cntlist[ord(cur)-ord('A')] += pow(10, i)
    i+=1
    item = item[:-1]

cntlist.sort(reverse=True)

result = 0

for i in range(9, 0, -1):
    result += i * cntlist[9-i]

print(result)
