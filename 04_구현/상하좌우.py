# -*- coding: utf-8 -*-
"""
- 여행가 A - 상, 하, 좌, 우 이동가능
- 시작 좌표 항상 1,1에서 시작.
- 정사각형을 벗어나면 [ 무시 ].
- L: 왼쪽으로 한칸 , R = 오른쪽으로 한칸, U = 위로 한칸, D = 아래로 한칸
  -( 0,-1 )        ( 0,1)               (-1,0)         (1,0)
"""


# 3-6.py 예시 
# N 공백을 기준으로 구분하여 입력 받기
n = int(input())
x,y = 1,1
plans = input().split()

# L, R, U, D에 따른 [ 이동 방향 ] 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_list = ['L','R','U','D'] # 정해져 있는 이동 계획서.
print(range(len(move_list)))

for plan in plans: # 입력받은 이동 계획을 [ 하나씩 확인 ] 
   for i in range(len(move_list)): #이동 후 좌표 구하기.
       # 입력 이동계획 하나와, 정해져 있는 움직이는 계획서와 비교해 [ 같다면 ]
       if plan == move_list[i]:
           # [ 시작 위치(1,1) ] 에 이동계획에 따른 좌표 값을 더해줘라.
             nx = x + dx[i]
             ny = y + dy[i]  
             
    # 정사각형 공간을 벗어나면 무시해라.
   if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
   print("여행가가 움직이는 위치 좌표 ",nx, ny)
   x,y = nx,ny  #이동 좌표를 수행해라 
print("[최종적]으로 도착할 지점의 좌표",x, y)