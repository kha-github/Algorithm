'''
손님에게 거슬러주어야 할 돈이 N 원일 때,
500, 100, 50, 10원 동전의 최소 개수를 구하라
가정1. 거슬러 주어야 할 돈 N은 항상 10의 배수임
'''

n = int(input("금액을 입력하세요 : ")) # 거슬러 줄 금액
cnt = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  cnt += n // coin # 거슬러줄 금액을 coin으로 나눠 해당 coin의 개수 구하기
  n %= coin


print(cnt)
