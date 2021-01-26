'''
첫번째 줄에는 몇 발자국만큼 이동할 건지,
다음 줄에는 R R R U D 와 같이 이동할 방향을 공백으로 구분하여 입력
시작 좌표는 (1,1) 이라면 이동한 후의 좌표의 위치는?
'''

n = input()
step = list(map(str, input()))

dx = [step.count('U')*-1, step.count('D')*1, 0, 0]
dy = [0, 0, step.count('L')*-1, step.count('R')*1]

x = 1
y = 1

for i in range(4):
  x = dx[i] + x
  y = dy[i] + y

print(str(x) + " " + str(y))
