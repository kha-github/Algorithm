n = int(input())
mylist = list(map(int, input().split()))
result_list = []
result_list.append(mylist[0])

for i in range(len(mylist)-1):
  result_list.append(max(result_list[i]+mylist[i+1], mylist[i+1]))

print(max(result_list))
