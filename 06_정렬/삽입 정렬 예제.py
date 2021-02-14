"""
p,161~164
6-3.py 코드
[삽입] 정렬
- 필요할 때만 위치를 바꾸므로 "데이터가 ** 거의 정렬 **되어 있을 때" 효율적
- 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 '삽입 정렬'이라고 부름.
※ [ 삽입 정렬 ]은 --> *** " 두 번째 데이터부터 시작 " **
   왜냐하면 " 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단 "하기 때문.
   
[ 정렬이 거의 되어있는 상황 ]에서는 '퀵 정렬' 알고리즘 보다 ' 더 강력 '하다.
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두번째 데이터 부터 시작.
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
         # 한 칸씩 왼쪽으로 이동
        if array[j] < array[j - 1]: # 왼쪽 인덱스값이 [ 오른쪽 인덱스 값보다 큰경우 ] 
            # 큰 값을 먼저 오른쪽에 저장한뒤
            # 작은 값을 왼쪽에 저장한다.
            array[j], array[j - 1] = array[j - 1], array[j] #작은 값을 한칸씩 왼쪽으로 이동.
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
