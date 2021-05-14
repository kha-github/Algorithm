n = int(input())
cnt = 0
value = 666
 
while cnt!=n:
  if str(value).find("666")!=-1:
    cnt+=1
  value+=1
  
print(value-1)
