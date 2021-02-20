"""
< 범위를 반씩 좁혀가는 탐색 > p. 186 ~ 187
- [ 리스트 내 ]에서 데이터를 매우 빠르게 탐색하는 [ 이진 탐색 알고리즘 ]

< '순차 탐색' 이란 ?> --> 순차로 데이터를 탐색
- 리스트 안에 있는 [ 특정한 데이터를 찾기 위해 ] 
  앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 보통 " 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 " 사용한다.

- 리스트 내에 데이터가 아무리 많아도 " 시간만 충분 "하다면 
  항상 원하는 원소(데이터) 를 찾을 수 있다는 장점.
- 리스트의 [ 데이터에 하나씩 방문 ]하며 특정한 문자열과 같은지 검사하므로 [ 구현도 간단 ].

< 사용되는 예 >
- 리스트에 [ 특정 값의 원소가 있는지 체크 ]할 때도 순차 탐색으로 원소를 확인
- 리스트 자료형에서 특정한 값을 가지는 " 원소의 개수를 세는 count() 메서드를 이용 "할 때도 
  내부에서 순차 탐색이 수행.
  
< 입력 >
5 Dongbin

Hanul Jonggu Dongbin Taeil Sangwook

< 출력 >
3
"""

# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 [ 하나씩 확인 ]하며
    for i in range(n):  # ex ) 5
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더하기)
    return -1 # 원소를 찾지 못한 경우 -1 반환

print("생성할 '원소 개수를 입력'한 다음 [한 칸 띄고 ] 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수  ex ) 5
target = input_data[1] # 찾고자 하는 문자열  ex) Dongbin

print("앞서 적은 [ 원소 개수만큼 문자열을 입력 ]하세요. 구분은 띄어쓰기 한 칸으로 합니다.")  
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))