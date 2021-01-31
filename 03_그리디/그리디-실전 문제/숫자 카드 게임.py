"""
# 행이 N, 열이 M
# 뽑고자 하는 행 선택
# 선택된 행 들중 숫자가 낮은 카드
# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수
"""
'''
####### 아래는 내가 푼 방법 ########
# N, M 공백을 기준으로 구분하여 입력 받기 (행, 열)
n, m = map(int, input().split())


#data= [[3,1,2],[4,1,4],[2,2,2]]

data2 = [[7,3,1,8],[3,3,3,4]]

min_value = 10001
min_list = []

for i in range(n):
   data = list(map(int,input().split()))
   if (min_value > min(data)):
        min_list.append(min(data))
        print(min_list)
print(max(min_list)) # 각 행마다 가장 작은 수중, [ 가장 높은 숫자가 쓰인 수를 출력 ].
'''

  
# N, M 공백을 기준으로 구분하여 입력 받기 (행, 열)
n, m = map(int, input().split())

#data= [[3,1,2],[4,1,4],[2,2,2]]
#data2 = [[7,3,1,8],[3,3,3,4]]

min_value = 10001
min_list = [] # 
result = []


for i in range(n): # 행
   data = list(input().split())
   for j in range(m): #열 
      min_list.append(int(data[j])) # 각 행을 저장받는다.
      
   if(min_value > min(min_list)): # [ 현재 행의 각 열에서 ] [ 가장 작은 수 ]를 찾기.
      result.append(min(min_list))   # 가장 작은 수를 출력에 쓰일 리스트 변수에 저장.
      min_list = [] # 현재 행을 초기화 시켜줌.
      print(result)
      
print("최종 정답은: %d" % max(result)) # 각 행마다 가장 작은 수중, [ 가장 높은 숫자가 쓰인 수를 출력 ].      

 
'''
책 정답
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    print(data)
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
'''