mystr = list(input())

mysum = 0
mynum = ""
isnegative = 1
isexcept = True

for i in range(len(mystr)):

  if mystr[i] == '-' or mystr[i] == '+':
    isexcept = False
    mysum +=  isnegative*int(mynum)
    mynum = ""
  else:
    mynum += mystr[i]

  if mystr[i] == '-':
    isnegative = -1


if isexcept:
  print(int(mynum))
elif isnegative == 1:
  print(mysum+int(mynum))
elif isnegative == -1:
  print(mysum-int(mynum))
