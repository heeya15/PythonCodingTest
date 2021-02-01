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

####### 아래는 내가 푼 방법 ########    - 4.8 초 , 4.5 초 

# N, M 공백을 기준으로 구분하여 입력 받기 (행, 열)
n, m = map(int, input().split())

#data1 = [[3,1,2],[4,1,4],[2,2,2]]
#data2 = [[7,3,1,8],[3,3,3,4]]


min_list = []
start_time = time.time() # 성능 측정 시작.
for i in range(n):
   data = list(map(int,input().split()))
   
   # 현재 줄에서 ' 가장 작은 수' 찾기.
   min_value = 10001
   if (min_value > min(data)):
        min_list.append(min(data))
        print(min_list)
        
end_time = time.time()  # 성능 측정 종료 .
print(max(min_list)) # 각 행마다 가장 작은 수중, [ 가장 높은 숫자가 쓰인 수를 출력 ].
print("성능 측정 : ", end_time-start_time)

#---------------------------------------------------------------------------------------

# N, M 공백을 기준으로 구분하여 입력 받기 (행, 열)  -- 5.2초, 5.05 초 
n, m = map(int, input().split())

#data= [[3,1,2],[4,1,4],[2,2,2]]
#data2 = [[7,3,1,8],[3,3,3,4]]

min_value = 10001
min_list = [] #각 행을 저장받는 리스트 초기화.
result = [] #출력에 쓰일 리스트 변수 초기화.

start_time = time.time() # 성능 측정 시작. 

for i in range(n): # 행
   data = list(input().split())
   for j in range(m): #열 
      min_list.append(int(data[j])) # 각 행을 저장받는다.
      
   if(min_value > min(min_list)): # [ 현재 행의 각 열에서 ] [ 가장 작은 수 ]를 찾기.
      result.append(min(min_list))   # 가장 작은 수를 출력에 쓰일 리스트 변수에 저장.
      min_list = [] # 현재 행을 초기화 시켜줌.
      print(result)
end_time = time.time() # 측정 종료 
print("최종 정답은: %d" % max(result)) # 각 행마다 가장 작은 수중, [ 가장 높은 숫자가 쓰인 수를 출력 ].      
print("성능 측정 : ", end_time-start_time)
