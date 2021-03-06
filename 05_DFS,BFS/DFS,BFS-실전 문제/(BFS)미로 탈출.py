"""
p,152 ~ p, 154

[ 알아 둘 점 ]
- 간선의 비용이 동일하다고 하면서
  최단 거리를 구하고자 할 때는 --> BFS(큐)를 사용하는것이 효과적(일반적으로)

- 만약 간선의 비용이 다르다고 하면
  다익스트라를 사용하는것이 일반적.  
5-11.py BFS 예제

# 탐색 알고리즘 - "너비" 우선 탐색 BFS
# [ 가까운 노드 ]부터 탐색하는 알고리즘
# 1. 탐색 시작을 노드를 "큐"에 삽입하고 방문처리를 한다
# 2. 큐에서 노드를 꺼내 [ 해당 노드의 인접 노드 중 ]에서 방문하지 않은 노드를  
    [ 모두 큐에 삽입 ]하고 [ 방문 처리 ]를 한다
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 수행한다
    
(실전 문제)미로 탈출 ( 괴물을 피해 탈출해야 함.)
# 첫째 줄에 최소 이동 칸의 개수를 출력
   - 시작 위치(1,1)
   - 한번에 한 칸씩 이동
   - 괴물 있는 칸 : 0
   - 괴물 없는 칸 : 1
   
※ 단순히 [ 가장 오른쪽 아래 위치 ]로 이동하는 것을 요구.]
  즉, graph[n-1][m-1] 위치까지 이동칸의 개수를 요구함.
★ 따라서, 매번 가까운 노드에 갈때마다 '이전 까지의 거리에다가'
   1을 더함으로써 최단 거리를 측정할 수 있다.
[ 입력 ]        [ 출력 ]
3 3        

110               5

010

011

"""
# 덱 라이브러리라고 부른다.
from collections import deque # 큐(Queue) 구현을 위해 [ deque 라이브러리 사용 ]

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = list(map(int,input().split()))


# 2차원 리스트의 맵 정보 입력 받기
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

# 북 ,동 , 남, 서 방향 정의 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 함수 정의
def bfs(x, y): 
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque() 
    queue.append((x,y)) # 시작노드를 [ 큐에 삽입 ]. (하나의 묶음 튜플로 넣음.)
    #print(queue)
    
    # 큐가 **  [ 비어있을 ]  ** 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()  # 제일 왼쪽 값을 꺼낸다.
        print(x,y)
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx< 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시(괴물이 있는 부분.)
            if graph[nx][ny] == 0: 
                continue
            
            # 해당 노드를 처음 방문 하는 경우에만 최단 거리 기록, 그 후, [ 시작점 제외 ]
            if graph[nx][ny] == 1 and (nx, ny) !=(0,0):
                #노드를 방문하는 경우 '이전 까지의 거리에다가 '1'을 더함
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx, ny))
                #print(queue)  # -- 흐름 확인용 '큐' 출력.
    # 가장 오른쪽 아래까지의 최단 거리 반환 ( 가장 오른쪽 아래 위치로 이동한 거리 반환.)
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))


