"""
p, 99
- 어떠한 수 N이 1이 될 때까지 [ 다음의 두 과정 중 하나를 반복적 ]으로 [ 선택 ]하여 수행.
- 단, [ 두 번째 연산 ]은 N이 K로 나누어떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다
2. N을 K로 나눈다.

예시)
N = 17, K = 4
- 나누어 떨어지지 않기에 1번과정 선택   --> N = 16
- 나누어 떨어짐 2번 선택  --> N = 4
- 나누어 떨어짐 2번 선택  --> N = 1    --> 총 전체 과정을 실행한 횟수는 '3' 

[ 문제 ]
- [ N과 K가 주어질 때 ] ' N이 1이 될 때까지 ' 1번 혹은 2번의 과정을 수행해야하는
 [ 최소 횟수를 구하는 프로그램 ] 작성하시오.
 
 [ 입력 ]           [ 출력 ]
 25 5                  2
"""

#######-------------  아래는 내가 푼 방법----------------  ########    

# N, K 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0


# N이 K이상 이라면 [ 아래 과정 계속 수행 ]하기. 
while True:  
    if n < k:  # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        break
    if n % k != 0:  # n이 k로 나누어 떨어지지 않으면 'N에서 1씩빼고' [ 횟수 +1 ]
          n -= 1
          result +=1
    elif n % k == 0: # n이 k로 나누어 떨어지면 [ 나눈 몫을 N값으로 정함. ]
          n //=k
          result +=1
# 마지막으로 남은 수에 대하여 1씩 빼기 -->
# 25 ,3 일경우  n= 2가되면 k보다 작은경우여서 나누기x , 따라서 1을빼야함.
          
while n > 1: # n이 1보다 클 경우에만 true
    n -= 1
    result += 1
                 
print(result) # 최소 횟수 정답.

#-----------------------------------------------------------------------------------------------

# 책 답안
# 단순하게 푸는 답안 예시 )
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0


# ' N이 K 이상이라면 ' K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 [ N에서 1씩 빼기 ]
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k # 나눈 몫을 n에 저장받음
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기 
# --> 25 ,3 일경우  n= 2가되면 k보다 작은경우여서 나누기x , 따라서 1을빼야함.
while n > 1: 
    n -= 1
    result += 1

print(result) # 최소 횟수 정답.

#---------------------------------------------------------------------------------------
# 3-6.py 예시 
# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 '남은 수(N)에 대하여' 1씩 빼기
result += (n - 1)
print(result) # 최소 횟수 정답.
