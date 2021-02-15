"""
p,171 ~ 175
6-6.py 코드
[계수]정렬 --> ＊ 특정한 조건이 부합 ＊ 할 때만 사용할 수 있다.
          --> 조건이 부합 할때 사용하며, 매우 빠른 정렬 알고리즘.
※ 별도의 리스트를 선언하고, 그 안에 " 정렬에 대한 정보를 담는다는 특징 "이 있다.
   " 데이터 크기가 제한 "되어 있을 때에 한해서 
   데이터 개수가 매우 많더라도 ★ 빠르게 동작 ★한다. 
    
 - 데이터의 값이 무한한 범위를 가질 수 있는 [ 실수형 데이터가 주어지는 경우 ] 
   계수 정렬은 사용하기 어려움.
   
 - 일반적으로 " 가장 큰 데이터 "와 " 가장 작은 데이터 "의 차이가 
   1,000,000(백만)을 넘지 않을 때 효과적으로 사용. 
    
 - 가장 큰 데이터와 가장 작은 [ ★ 데이터의 차이가 너무 크다면 ] 계수 정렬은 사용 x  
  
 - 계수 정렬을 이용할 때는 '모든 범위를 담을 수 있는'
   크기의 리스트(배열)을 선언
   
- 가장 큰 데이터와 가장 작은 [ 데이터의 차이가 100 ]이라면 
  101개의 데이터가 들어갈 수 있는 리스트를 초기화 해야 한다.
  ※여기서 1을 더해주는 이유는 < 0부터 100까지는 총 101개의 수가 존재 >하기 때문
  
- 비교 기반의 정렬 알고리즘 x
"""

# 내가 푼 방법.
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 파이썬에는 리스트를 한 줄의 코드로 손쉽게 만들 수 있는 list comprehension이라는 문법 사용.
count = [0 * i for i in range(10)]

for i in range(len(array)):
    count[array[i]] +=1
    
print(count)

for j in range(len(count)):
    for k in range(count[j]):
        print(j ,end=' ')

#----------------------------------------------------------------------------------
        
# 6-6.py 책 정답.       
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # "띄어쓰기를 구분"으로 [ 등장한 횟수만큼 ] 인덱스 출력
        