"""
재귀 함수를 사용했을때의 장점
- 반복문 보다 [ 코드가 더 간결 ]하다.
이유: 수학의 점화식(재귀식)을 그대로 소스코드로 옮겼기 때문이다.
"""


# 반복적으로 구현한 n!
def factorial_iterative(n):        
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
       result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):        
    if n <= 1: # n이 1 [ 이하 ]인 경우 [ 1을 반환 ]
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))