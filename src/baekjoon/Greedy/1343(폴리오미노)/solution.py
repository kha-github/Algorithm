mystr = list(input().split('.'))

result = ""

for item in mystr:
  result += "."
  if len(item)%4 == 0:
    result += item.replace('X','A')
  elif len(item)%4 == 2:
    result += item[0:len(item)-2].replace('X','A')
    result += item[len(item)-2:len(item)].replace('X','B')
  else:
    print(-1)
    exit(0)

print(result[1:])
