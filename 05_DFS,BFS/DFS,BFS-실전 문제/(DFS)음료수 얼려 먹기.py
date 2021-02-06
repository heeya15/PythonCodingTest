"""
p,149 ~ p, 151
5-10.py DFS 예제
# 탐색 알고리즘 - 깊이우선탐색 DFS
- '[ 가장 깊숙이 위치하는 노드에 닿을 때 ]'까지 확인(탐색) 하면 된다. 
# 1. 탐색 시작 노드를 [ 스택에 삽입 ]하고 방문 처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 
     그 인접 노드를 스택에 넣고 방문 처리를 한다. 
    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. [ 2번의 과정을 더 이상 수행할 수 없을 때까지 ] 반복한다.
---------------------------------------------------------------
# 구멍이 뚫려 있는 부분 끼리 상, 하, 좌, 우로 붙어 있는 경우
  [ 서로 연결되어 있는 것으로 간주 ]한다.
-> 즉, 인덱스의 값이 [ 0으로 되어있는것 끼리 ] 
   상,하 좌 우 붙어 있으면 서로 하나의 연결로 간주 .
[ 입력 조건 ]
- '첫'번째 줄 N(세로), M(가로)을 입력 
- '두'번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어진다.
- 이때 "구멍이 뚫려있는 부분"은 '0', "그렇지 않은 부분"은 '1'이다.

[ 출력 조건 ]
- 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
"""
# 앞에 배웠던 내용으로 조합하여 풀어봤다.

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int,input().split())

graph = []

#2차원 리스트 얼음 틀 형태 입력. (맵을 입력 .)
for k in range(n):
    graph.append(list(map(int,input())))
 
# 상 우 하 좌 정의 .
dx =[-1, 0, 1, 0]
dy =[0, 1, 0, -1]
  

# 맵, x,y좌표 값, 방문 정보를 인수로 넘겨 받음.
def dfs(graph, i, j, visited):    
    print(i,j)
    print(sep='\n')
    for k in range(4): # 상 우 하 좌 붙어있는지 검사. 
        x = i + dx[k]
        y = j + dy[k]
        
        # 주어진 범위를 벗어나는 경우에는 무시 .
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        # 칸막이 부분, [방문했던 부분]은 무시 .
        if graph[x][y] == 1 or visited[x][y] == True:
            continue
        
        # 범위를 벗어 나지 않는 경우. 해당 노드 방문 처리 .
        else:
            visited[x][y] = True
            dfs(graph, x, y, visited)



# 각 노드가 [ 방문된 정보를 리스트 자료형으로 표현 ](2차원 리스트)
visited = []
for i in range(n):
    visited.append([False] * m)


# 만들수 있는 " 얼음덩이 수 "를 세기위한 변수 .
count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            count += 1
            visited[i][j] = True #0,0 인덱스는 바로 방문 처리.
            dfs(graph, i, j, visited)

print("만들수 있는 얼음 덩이 :", count)


#------------------------------------------------------------------
# ** 책정답 ** 5-10.py 

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print("만들수 있는 얼음 덩이 :", count)


