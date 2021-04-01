def getFibo(value):
  global fiboList
  i = 1

  while True:
    if fiboList[i] > value:
      return fiboList[i-1]
    elif i == len(fiboList)-1:
      fiboList.append(fiboList[i]+fiboList[i-1])
    i+=1

n = int(input())

fiboList = [0, 1]

for _ in range(n):
  target = int(input())
  result = []
  while target != 0:
    ret = getFibo(target)
    result.append(ret)
    target -= ret
  result.sort()
  result = list(map(str, result))
  print(" ".join(result))
