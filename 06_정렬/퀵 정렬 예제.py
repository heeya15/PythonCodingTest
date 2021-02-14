'''

p,164 ~ 170
6-4.py 코드
[퀵]정렬 --> 실제로 [ 재귀 함수 형태로 작성 ]했을 때 구현이 매우 간결.

- 지금까지 배운 정렬 알고리즘 중에 [ 가장 많이 사용되는 알고리즘 ].
- 이 알고리즘은 대부분의 프로그래밍 언어에서 [ 정렬 라이브러리의 근간 ]이 되는 알고리즘.
- 기준 데이터를  설정한 다음 '큰 수' 와 '작은 수'를 [ 교환한 후 ] 
  [ 리스트를 반으로 나누는 방식 ]으로 동작

- 퀵 정렬에서는 [ ** 피벗(Pivot) ** ] 이 사용된다.
  '큰 숫자'와 '작은 숫자'를 교환할 때, [ 교환하기 위한 '기준'을 바로 피벗 ]이라고 표현.

- [ 퀵 정렬을 수행하기 전 ]에는 "피벗"을 어떻게 설정할 것인지 [ 미리 명시 ]해야 한다.

- 책에서는 가장 대표적인 분할 방식인 [ 호어 분할 방식 ]을 기준으로 퀵 정렬 설명

[ "호어 분할 방식" 에서는 다음과 같은 규칙에 따라서 피벗을 설정]
 - 리스트에서 [ "첫 번째 데이터"를 피벗 ]으로 설정.
 - < 피벗을 설장한 뒤 > 
   [ 왼쪽 ]에서 피벗보다 [ 큰 데이터 ]를 찾고
   [ 오른쪽 ]에서 피벗보다 [ 작은 데이터 ]를 찾는다.
 - 그 다음 큰 데이터와 작은 데이터의 위치를 서로 교환해준다.
 - 이러한 과정을 반복하면 '피벗'에 대해 정렬이 수행.
 
'''
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 책 정답. 6-4.py 퀵 정렬 소스 코드  (p, 168)
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # '피벗' 은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 '큰' 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 '작은' 데이터를 찾을 때까지 반복
        # 피벗보다 [ 배열 right인덱스 값 ]이 더 크다면 아래 수행.
        while(right > start and array[right] >= array[pivot]): 
            right -= 1
        
        if(left > right): # 엇갈렸다면 [ 작은 ] 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
            
        else: # 엇갈리지 않았다면 [ 작은 데이터 ]와 [ 큰 데이터 ]를 교체
            array[left], array[right] = array[right], array[left]
        print(left,right)
        print(array) # 선택된 것을 확인하기 위한 출력문.
   
    # [ 분할 이후 ] 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    
    quick_sort(array, start, right - 1)
    # 아래는 [ 오른쪽 부분에서 ] 정렬 수행.
    quick_sort(array, right +1, end) # 두번째 인수 right +1 or left로 두어도 된다.

quick_sort(array, 0, len(array) - 1)
print("퀵 정렬 수행된 결과:",array)

#--------------------------------------------------------------------------------
#6.5.py [ 파이썬의 **장점**을 살린 ] 퀵 정렬 소스코드 (p, 169)

# 단 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로 [ 시간 면에서는 조금 비효율적 ]
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 '첫' 번째 원소
    tail = array[1:] # [ 피벗을 제외 ]한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 [왼쪽] 부분--> 피벗보다 작거나 같은것.
    print(left_side)
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분--> 피벗보다 큰 
    print(right_side)
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, [ 전체 리스트를 반환 ]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print("퀵 정렬 수행된 결과:", quick_sort(array))