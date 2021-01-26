while(True): 
  number = input()
  check = 0

  if (number == "0"):
    break
  
  for i in range(len(number)//2):
    if (number[i] != number[-(i+1)]):
      print("no")
      check = 1
      break
  if (check != 1):
    print("yes")
