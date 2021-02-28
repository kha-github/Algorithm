m, q = map(int, input().split())

poketmon_list = []
poketmon_dic = {}

for i in range(m):
  poketmon_list.append(input())
  poketmon_dic[poketmon_list[-1]] = i+1

for _ in range(q):
  temp = input()
  if temp.isdigit():
    print(poketmon_list[int(temp)-1])
  else:
    print(poketmon_dic[temp])

