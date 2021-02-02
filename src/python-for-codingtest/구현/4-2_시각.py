n = int(input())

cnt = 0

for hour in range(n+1):
  for min in range(60):
    for sec in range(60):
      mystr = str(hour).zfill(2) + str(min).zfill(2) + str(sec).zfill(2)
      if mystr.count('3') != 0:
        cnt += 1

print(cnt)
