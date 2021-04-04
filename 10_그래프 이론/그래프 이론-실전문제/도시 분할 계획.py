"""
(실전 문제) 도시 분할 계획 p, 300

- 마을은 [ N개의 집 ]과 그 '집'들을 [ 연결하는 M개 ]의 '길'로 이루어져 있다. 

- '길은' 어느 방향으로든지 다닐 수 있는 편리한 길이다. 그리고 '각 길'마다 '길을 유지'하는데 드는 [ 유지비 ]가 있다.

- 마을의 이장은 마을을 [ "두 개의 분리된 마을로 분할할 계획" ]을 가지고 있다.
 
- 마을을 분할할 때는 [ 각 분리된 마을 안에 ] ' 집들이 ** 서로 연결되도록 분할 ** '해야 한다.
- 각 [ 분리된 마을 안에 있는 ] ' ** 임의의 두 집 사이 ** '에 [ 경로가 항상 존재해야 한다는 뜻 ]이다. 
  마을에는 [ 집이 하나 이상 있어야 ] 한다.

- 그렇게 마을의 이장은 계획을 세우다가 마을 안에 [ 길이 너무 많다는 생각 ]을 하게 되었다. 

- 일단 분리된 [ 두 마을 사이에 있는 길들은 ] 필요가 없으므로 [ 없앨 수 있다 ]. 

- 그리고 [ 각 분리된 마을 안에서도 ] 임의의 두 집 사이에 ' 경로가 항상 존재하게 하면서 ' 길을 더 없앨 수 있다.
 
- 마을의 이장은 위 조건을 만족하도록 [ 길들을 모두 없애고 ] 
 ' 나머지 길 유지비의 합을 ** 최소 ** '로 하고 싶다. 이것을 구하는 프로그램을 작성하시오.
------------------------------------------------------------------------------
[ 입력 조건 ]

- 첫째 줄에 [ 집의 개수 ] N , [ 길의 개수 ] M 이 주어진다.
  N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수이다.

- 그 다음 줄부터 M 줄에 걸쳐 [ 길의 정보가 ] A B C 세 개의 정수로 주어지는데 
  A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000)라는 뜻이다.
  

[ 출력 조건 ]

- 첫째 줄에 길을 없애고 [ 남은 길 유지비의 ] 합의 '최솟값을 출력'한다.

( 아이 디어 )
- 2개의 최소 신장 트리를 만들어야 한다는 것.

- 최소한의 비용으로 2개의 신장 트리로 분할하려면 어떻게?
  먼저, 크루스칼 알고리즘으로 (최소 신장 트리를 찾은 뒤에)
  최소 신장 트리를 구성하는 '간선' 중에서 [ ** 비용이 가장 큰 간선을 제거  ** ]
  그러면, 최소 신장 트리가 (2개의 부분 그래프로) 나누어짐.
"""
# 책 정답 10-8.py (p, 301~ 302)

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 [ 간선을 담을 리스트 ]와, [ 최종 비용을 담을 ] 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 [ 자기 자신으로 ] 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 '간선'에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # '비용순으로 정렬'하기 위해서 [ 튜플의 첫 번째 원소 ]를 '비용'으로 설정
    edges.append((cost, a, b))

# 간선을 [ 비용순(오름차순) ]으로 정렬
edges.sort()
print(edges)
last = 0 # [ 최소 신장 트리에 포함 ]되는 간선 중에서 '가장 비용이 큰 간선'

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # [ 사이클이 발생하지 않는 경우 ]에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost # [ 최종 비용에 ] 추가로 더함.
        last = cost # 결국에는 마지막의 비용이 last 변수에 저장. (즉, '가장 큰 비용'이 저장됨.)

print(result - last) # 최종 비용 - 가장 큰 비용 = (가장 먼 길이의 '길'을 제거 )즉, 길의 유지비의 합 [ 최소비용 ]