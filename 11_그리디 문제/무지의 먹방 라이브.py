"""
(실전 문제) 무지의 먹방 라이브 p, 316 ~ 317 

(입출력 예)

food_times	k	result
[3, 1, 2]	5	1

- food_times는 각 음식을 모두 먹는데 필요한 시간.
- k는 방송이 중단된 시간
- 만약 더 섭취해야 할 음식이 없다면 [ -1을 반환 ]
"""
'''
import heapq
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0 # [ 먹기 위해 ] 사용한 시간
    previous = 0 # 직전에 [ 다 먹은 음식 ] 시간
    length = len(food_times) # [ 남은 음식의 ] 개수
        
    answer = 0
    
    while q or 
    return answer

print(solution((3,1,2),5))

'''

# 책 정답 11-6.py ( p, 514 ) 
import heapq

def solution(food_times, k):
    # [ 전체 음식을 먹는 시간보다 ] k가 크거나 같다면 -1 --> 다음에 먹을 음식이 없기 때문.
    # 즉, [ 중단 될 시간안에 ] 음식을 다 먹는다면, 다음에 먹을 음식이 없어서 '-1'을 반환.
    if sum(food_times) <= k:
        return -1

    # [ 음식 시간이 작은 음식부터 ] 빼야 하므로 [ 우선순위 큐를 이용 ]
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 '우선순위 큐에 삽입'
        heapq.heappush(q, (food_times[i], i + 1)) 
       
    sum_value = 0 # [ 음식을 먹기 위해 사용한 ] 시간
    previous = 0 # [ 직전(이전)에 다 먹은] 음식 시간
    length = len(food_times) # [ 남은 음식의 개수 ]

 # sum_value(먹기위해 사용한 시간) + {{(현재의 음식 시간 - 이전 음식 시간)} * 현재(남은) 음식 개수}와 [ k 비교 ]
    while sum_value + ((q[0][0] - previous) * length) <= k:  # 즉, 중단 될 시간과, 같거나, 작을 경우만 반복.       
        now = heapq.heappop(q)[0] # [ 적게 걸리는 음식 시간부터 ] 들고옴.
        # (처음 시간 - 이전 시간) * 남은 음식 갯수. --> 이게 k에서 뺄수 있는 값이 된다.
        sum_value += (now - previous) * length 
        length -= 1 # < 다 먹은 음식 '제외' >
        previous = now # 이전 [ 음식 시간을 (현재 시간으로 )재설정 ]
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # [ ** 음식의 번호 ** 기준 ]으로 정렬
    
    #( k(중단될 시간) - sum_value(먹기위해 사용한 시간) % 남은 음식갯수 
    # 만약 4 % 3 = 1 이되는데, 이게 2, 4, 5 번 음식이 남아 있다고 가정했을때
    # 3이라는 시간을 쓰고 다시 맨처음 '2'로 돌아오고나서, 중지가 된뒤 다음의 다시먹을 음식번호가 '4'가 됨.
    return result[(k - sum_value) % length][1] # 다시먹을 [ '음식 번호'를 출력함. ] --> 그래서 [1]을 고정시켜 놓음.

print("다시 먹을 음식 번호는 : ", solution((3,1,2),5))

print("다시 먹을 음식 번호는 : ", solution((3,5,1,6,5,3),20))