import time
"""
[ 문제 ]
- 여러 개의 숫자 카드 중 [ 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 ] 게임

< 게임의 룰은 다음과 같다. >

- 숫자가 쓰인 카드들이 N * M 형태로 놓여있다. (N은 행의 수, M은 열의 수)
- 먼저 뽑으려는 카드가 포함되어 있는 행을 선택
- 그 다음 [ 선택된 행에 포함된 카드 중  ] [ 가장 낮은 카드를 뽑아야 ] 한다.
- 가장 낮은 숫자 카드중 [ 가장 높은 숫자가 쓰인 카드 한장을 뽑아야 ]함.
[ 해결 방법 ]
- 각 행에서 가장 작은 수를 찾은 후, 그 수 중에서 [ 가장 큰 수 한장을 찾는 방식 ]으로 문제를 해결.
"""

#책 정답(1) -- min() 함수를 이용하는 답안 예시   9초, 5.7초 
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0 
# 한 줄씩 입력 받아 확인하기
start_time = time.time()
for i in range(n):
    data = list(map(int, input().split()))
    print(data)
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
end_time = time.time() 
print(result) # 최종 답안 출력
print("성능 측정 : ", end_time-start_time)

#---------------------------------------------------------------------------------------

#책 정답(2)  --[ 2중 반복문 구조 ]를 이용하는 예시    6.6초, 5.5초 

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0 
# 한 줄씩 입력 받아 확인하기
start_time = time.time() # 성능 측정 시작. 
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    
    for a in data:
        min_value = min(min_value,a)
        
    # '가장 작은 수'들 중에서 가장 큰 수 찾기.
    result = max(result, min_value)
    
end_time = time.time() # 측정 종료 .
print(result) # 최종 답안 출력
print("성능 측정 : ", end_time-start_time)