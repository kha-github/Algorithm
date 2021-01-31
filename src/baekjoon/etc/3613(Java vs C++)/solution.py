def fineUpper(targetStr):
  for i in range(len(targetStr)):
    if targetStr[i].isupper():
      return i
  
  return 0

def CppToJava(changeStr):
  
  while(changeStr.count('_') != 0):
    target = changeStr.find('_')
    changeStr = changeStr[0:target] + changeStr[target+1].upper() + changeStr[target+2:]
  
  return changeStr


def JavaToCpp(changeStr):
  
  while fineUpper(changeStr):
    target = fineUpper(changeStr)
    changeStr = changeStr[0:target] + "_" + changeStr[target].lower() + changeStr[target+1:]
  
  return changeStr

def check(targetStr):
  for i in mystr:
    if not(i.isalnum() or i == '_'):
      return -1
  return 1

mystr = input()

if check(mystr) == -1:
  print("Error!")

elif mystr.count('_') != 0 and mystr.islower() and mystr[-1]!="_" and mystr[0] != "_" and mystr.find("__")<0:
  print(CppToJava(mystr))

elif len(mystr) != 0 and mystr[0].islower() and mystr.count('_') == 0:
  print(JavaToCpp(mystr))

else:
  print("Error!")

