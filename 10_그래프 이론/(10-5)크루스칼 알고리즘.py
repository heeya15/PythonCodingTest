"""
( 신장 트리 ) p, 280

- 하나의 그래프가 있을 때 [ 모든 노드를 포함 ]
- 사이클이 존재 x

( 크루스칼 알고리즘 ) p, 281~283
- '최소 신장 트리 알고리즘' 중 하나
- [ 가장 적은 비용 ]으로 모든 노드를 연결 가능 
- 그리디 알고리즘으로 분류

(방법)
- 모든 간선에 대하여 '오름차순 정렬 '을 수행
- 가장 거리가 짧은 '간선' 부터 집합에 포함
- 사이클이 발생할 수 있는 '간선'의 경우 집합 포함 x

( 알고리즘 )
  1. 간선 데이터를 비용에 따라 [ 오름차순으로 정렬 ].
  
  2. 간선을 하나씩 확인하며 '현재의 간선이' 사이클을 발생하는지 확인.
     (1). [ 사이클이 발생하지 않는 경우 ] 최소 신장 트리에 [ 포함시킨다. ]
     (2). [ 사이클이 발생하는 경우 ] 최소 신장 트리에 [ 포함시키지 않는다. ]
  3. 모든 간선에 대하여 (2번의 과정을 반복한다.)

- 최종적으로 신장 트리에 포함되는 간선의 개수가 '노드의 개수 -1'과 같다는 특징
ex) 노드의 개수가 7이면 --> 최종적으로 [ 신장 트리에 포함되는 간선의 개수 ]는 '6'이다. 
 
"""

# 책 정답 10-5.py (p, 288~289 )
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, [ 루트 노드를 찾을 때까지 ] '재귀적'으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 [ 속한 집합 ]을 '합치기' --> 큰 번호를 갖는 노드를 [ 작은 번호 노드로 ] 부모 변경.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# [ 노드의 개수 ]와 [ 간선(Union 연산)의 개수 ] 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # [ 부모 테이블 초기화 ]하기

# 모든 [ 간선을 담을 리스트 ]와, [ 최종 비용을 담을 ] 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 [ 자기 자신으로 ] 초기화
for i in range(1, v + 1):
    parent[i] = i

# [ 모든 '간선'에 대한 정보 ]를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # [ **  비용순으로 정렬 ** ]하기 위해서 ' 튜플의 첫 번째 원소를 비용 '으로 설정
    edges.append((cost, a, b))

# '간선'을 [ 비용순으로 정렬( 오름 차순 ) ]
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge # 비용, 간선을 옆 변수에 저장.
    
    # [ 사이클이 발생하지 않는 경우 ]에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost  # [ 최종 비용에 ] 추가로 더함.
        
print("최소 신장 트리를 만드는데 필요한 비용 :" + str(result))

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')