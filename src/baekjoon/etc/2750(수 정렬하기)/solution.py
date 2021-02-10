def Insertion(mylist):
  
  for i in range(0, len(mylist)):
    
    my_max = mylist[0]

    for k in range(1, len(mylist)-i):
      if(mylist[k] < my_max):
        mylist[k-1] = mylist[k]
      else:
        mylist[k-1] = my_max
        my_max = mylist[k]
    
    mylist[len(mylist)-i-1] = my_max

  return mylist


n = int(input())

mylist = []

for i in range(n):
  mylist.append(int(input()))

mylist = Insertion(mylist)

for item in mylist:
  print(item)
