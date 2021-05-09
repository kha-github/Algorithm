def fun(oplist, val):

  global mylist
  
  stack = [{'oplist': oplist, 'val': val, 'cur': 1}, ]

  while stack:
    temp = stack.pop()
    oplist = temp['oplist']
    val = temp['val']
    cur = temp['cur']

    if sum(oplist) == 0:
      resultlist.append(val)
    
    if oplist[0] > 0:
      newlist = [oplist[0]-1, oplist[1], oplist[2], oplist[3]]
      stack.append({'oplist': newlist, 'val':val + mylist[cur], 'cur': cur+1})
    if oplist[1] > 0:
      newlist = [oplist[0], oplist[1]-1, oplist[2], oplist[3]]
      stack.append({'oplist': newlist, 'val':val - mylist[cur], 'cur': cur+1})
    if oplist[2] > 0:
      newlist = [oplist[0], oplist[1], oplist[2]-1, oplist[3]]
      stack.append({'oplist': newlist, 'val':val * mylist[cur], 'cur': cur+1})
    if oplist[3] > 0:
      newlist = [oplist[0], oplist[1], oplist[2], oplist[3]-1]
      stack.append({'oplist': newlist, 'val':int(val / mylist[cur]), 'cur': cur+1})




n = int(input())
mylist = list(map(int, input().split()))
input_oplist = list(map(int, input().split()))
resultlist = []

fun(input_oplist, mylist[0])

print(max(resultlist))
print(min(resultlist))
