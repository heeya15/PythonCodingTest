"""
p, 143 ~147 
5-9.py BFS 예제
# 탐색 알고리즘 - "너비" 우선 탐색 BFS
# [ 가까운 노드 ]부터 탐색하는 알고리즘
# 1. 탐색 시작을 노드를 "큐"에 삽입하고 방문처리를 한다
# 2. 큐에서 노드를 꺼내 [ 해당 노드의 인접 노드 중 ]에서 방문하지 않은 노드를  
    [ 모두 큐에 삽입 ]하고 [ 방문 처리 ]를 한다
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 수행한다

"""

from collections import deque # 큐(Queue) 구현을 위해 [ deque 라이브러리 사용 ]

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start]) # 시작노드를 [ 큐에 삽입 ].
    
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 **  [ 비어있을 ]  ** 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()  # 제일 왼쪽 값을 꺼낸다.
        print(v, end=' ')
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]: # 해당 노드와 "인접된 노드"중 [ 방문하지 않았을경우 ]  
                queue.append(i)  # 큐에 추가한다.
                visited[i] = True # 그리고 방문 처리를 한다. 

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 [ BFS 함수 호출 ]
bfs(graph, 1, visited)
