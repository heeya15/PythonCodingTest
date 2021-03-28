"""
(서로소 집합) p, 268
- 공통 원소가 '없는' 두 집합을 의미
ex) 집합{1,2}, {3,4} 는 '서로소 관계'다.

< 서로소 집합 자료구조 >

- [ 서로소 부분 집합들로 나누어진 ] 원소들의 데이터를 처리하기 위한 자료구조.

- 서로소 집합 자료구조는 '합집합(union)' 연산, '찾기(find)' 연산으로 조작

합집합(UNION) 연산 : '2개의 원소가 포함된 집합'을 [ 하나의 집합으로 합치는 ] 연산
찾기(FIND) 연산 : '특정한 원소'가 속한 집합이 [ 어떤 집합인지 알려주는 ] 연산
- 두 집합이 [ 서로소 관계인지를 확인할 수 있다는 말 ]은 
  '각 집합'이 [ 어떤 원소를 공통으로 가지고 있는지를 확인 ]할 수 있다는 말과 같기 때문.

[ '트리 자료구조를 이용' 해서 ' 서로소 집합 계산 ' 알고리즘 ]

1. 합집합 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인
   (1). A와 B의 [ 루트 노드 ] A', B'를 각각 찾는다.
   (2). A'를 B'의 부모 노드로 설정. (B'가 A'를 가리키도록 한다.)
2. 모든 UNION 연산을 처리할 때까지 1번 과정을 반복.

- 또한 실제로 구현할 때는 A'와 B'중에서 [ 더 번호가 작은 원소 ]가 '부모 노드'가 되도록 구현
"""

# 책 정답 10-1.py (p, 273 )
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# [ 노드의 개수 ]와 [ 간선(Union 연산)의 개수 ] 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # '부모 테이블 초기화'하기

# 부모 테이블상에서, 부모를 [ 자기 자신으로 ] 초기화
for i in range(1, v + 1):
    parent[i] = i

# [ Union 연산 ]을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# [ 각 원소가 속한 ] '집합' 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')


