"""
p,152 ~ p, 154
5-11.py BFS 예제

# 탐색 알고리즘 - "너비" 우선 탐색 BFS
# [ 가까운 노드 ]부터 탐색하는 알고리즘
# 1. 탐색 시작을 노드를 "큐"에 삽입하고 방문처리를 한다
# 2. 큐에서 노드를 꺼내 [ 해당 노드의 인접 노드 중 ]에서 방문하지 않은 노드를  
    [ 모두 큐에 삽입 ]하고 [ 방문 처리 ]를 한다
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 수행한다
    
(실전 문제)미로 탈출
# 첫째 줄에 최소 이동 칸의 개수를 출력
- 시작 위치(1,1)
- 한번에 한 칸씩 이동
- 괴물 있는 칸 : 0
- 괴물 없는 칸 : 1

[ 입력 ]
3 3

110

010

011
[ 출력 ]
5
"""

from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([[0, 0, 1]])  # 위치와 이동 횟수 정보 저장
    print(queue)
    while queue:
        x, y, cnt = queue.popleft()
        print(queue)
        if x == N - 1 and y == M - 1:  # 목표 지점 도달
            return cnt
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if arr[nx][ny] == 0:
                    continue
                if arr[nx][ny] == 1 and (nx, ny) != (0, 0):  # 해당 노드를 처음 방문 하는 경우에만 최단 거리 기록, 시작점 제외
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append([nx, ny, cnt + 1])
                    print(queue)


# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]


# BFS 탐색
print(bfs())
'''
from collections import deque # 큐(Queue) 구현을 위해 [ deque 라이브러리 사용 ]
# 상 우 하 좌 정의 .
dx =[-1, 0, 1, 0]
dy =[0, 1, 0, -1]
# BFS 함수 정의



# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int,input().split())

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))
    
def bfs(graph, x, y, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([graph]) # 시작노드를 [ 큐에 삽입 ].
    
    # 현재 노드를 방문 처리
    visited[x][y] = True
    count=0
    # 큐가 **  [ 비어있을 ]  ** 때까지 반복
    while queue:
        
        for k in range(4): # 상 우 하 좌 붙어있는지 검사. 
            nx = x + dx[k]
            ny = y + dy[k]
        
            # 주어진 범위를 벗어나는 경우에는 무시 .
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물 있는곳은 무시.
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
               count +=1
               print(count)
       

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(2차원 리스트)
visited =[]
for _ in range(n):
   visited.append([False] * m)

print(visited)

# 정의된 [ BFS 함수 호출 ]
bfs(graph, 0,0, visited)
'''