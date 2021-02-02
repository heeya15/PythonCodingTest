
'''
나이트가 이동할 수 있는 경우의 수를 출력.
- 8*8 좌표 정원 밖으로 나갈수 없음.
< 나이트는 특정한 위치에서 [ 다음과 같은 2가지의 경우로 이동 ]할 수 있다.>
1. "수평으로 두 칸" 이동한 뒤에 "수직"으로 한 칸 이동
2. "수직으로 두 칸" 이동한 뒤에 "수평"으로 한 칸 이동


입력 : a1       c2
출력 : 2        6

ord() 함수 = 특정한 문자를 아스키코드값으로 변환. 

'''
#  내가 푼 방법.
# 4-3.py 예시 
# N 현재 나이트의 위치 입력 받기.
input_data= input()
row = int(input_data[1]) # 행 추출 
col = input_data[0]      # 열 추출 

# '열'에 대한 [ 좌표값을 구하는 ] 조건문.
if col=='a':
   col = 1
elif col=='b':
     col = 2
elif col=='c':
     col=3
elif col=='d':
     col=4
elif col=='e':
     col=5
elif col=='f':
     col=6
elif col=='g':
     col=7
elif col=='h':
     col=8

print(row, col)
# 상, 하, 좌, 우 규칙에 따른 [ 8가지 방향에 대하여 정의 ] 
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

result = 0

for i in range(len(dx)): #이동 후 좌표 구하기.  
    # 이동하고자 하는 위치 확인 
     nx = row + dx[i]
     ny = col + dy[i]  
            
     # x가 1보다 크고 y도 1보다크고 
     # x가 8보다 작고 y도 8보다 작으면 카운터 증가. 
     # 즉, 8*8 좌표 "평면 범위를 나가지 않는경우" [ 횟수를 증가 시킨다. ]
     if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
         result += 1 

print("[최종적]으로 도착할 지점의 좌표",result)


# -------------------------------------------------------------------------
# 책 답안  4-3.py  -- p, 117

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])

column = (int(ord(input_data[0])) - int(ord('a'))) + 1
print(row, column)
# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

