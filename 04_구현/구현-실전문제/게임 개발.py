"""
 1 1 1 1   - 모두 바다
 1 0 0 1   - 바다/ 육지/ 육지/ 바다
 1 1 0 1   - 바다 / 바다/ 육지/ 바다
 1 1 1 1   - 모두 바다.
 
************ 아직 정확히 내것이 아니여서 다시 한번 보자..! *******
"""
# 4-4.py  p, 120쪽 책 정답. 
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

        
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# [ 방문한 위치를 저장 ]하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
print(d)

# 현재 캐릭터의 'X 좌표, Y 좌표', [ 바라보는 방향] 을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# [ 전체 맵 정보 ]를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    # 반 시계방향을 위해서.
    if direction == -1: #방향이 -1인경우 -->' 서쪽' 방향으로 정의 해라.
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # "회전한 이후" 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    #  네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)