import collections

def BFS():
  move_x = [0, 0, 1, -1]
  move_y = [1, -1, 0, 0]

  waterq = collections.deque()
  for item in water_loc:
    waterq.append(item)

  cnt = 0

  animalq = collections.deque()
  animalq.append(animal_loc)

  next_waterq = collections.deque()
  next_animalq = collections.deque()

  while(True):

    cnt += 1

    while(waterq):
      water_cur = waterq.pop()
      for i in range(4):
        water_x = water_cur[0] + move_x[i]
        water_y = water_cur[1] + move_y[i]

        if water_x >= 0 and water_y >= 0 and water_x < r and water_y < c:
          if mylist[water_x][water_y] == '.' or mylist[water_x][water_y] == 'S':
            next_waterq.append((water_x, water_y))
            mylist[water_x][water_y] = '*'

    while(animalq):
      animal_cur = animalq.pop()
      for i in range(4):
        animal_x = animal_cur[0] + move_x[i]
        animal_y = animal_cur[1] + move_y[i]

        if animal_x >= 0 and animal_y >= 0 and animal_x < r and animal_y < c:
          if mylist[animal_x][animal_y] == '.':
            next_animalq.append((animal_x, animal_y))
            mylist[animal_x][animal_y] = 'S'
          if mylist[animal_x][animal_y] == 'D':
            return cnt
    if len(next_animalq) == 0:
      return "KAKTUS"
      
    waterq = next_waterq
    animalq = next_animalq
    next_waterq = []
    next_animalq = []
    

    

r, c = map(int, input().split())

mylist = []
water_loc = []

for i in range(r):
  temp = list(input())
  mylist.append(temp)
  for k in range(c):
    if temp[k] == 'S':
      animal_loc = (i, k)
    elif temp[k] == '*':
      water_loc.append((i, k))
    elif temp[k] == 'D':
      target_loc = (i, k)

print(BFS())
