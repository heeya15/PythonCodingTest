"""

p, 210 
# 수학적 점화식을 프로그래밍으로 표현하려면 [ 재귀 함수를 사용 ]하면 간단
  예시를 소스코드로 바꾸면 다음과 같다.
"""

# 8-1.py [ 피보나치 함수 ] 소스코드
# 피보나치 함수(Fibonacci Function )를 [ 재귀 함수로 구현 ]
def fibo(n) :
    if n ==1 or n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)

print(fibo(4))
'''
- 그런데 피보나치 수열의 소스코드를 [ 위와 같이 작성 ]하면 심각한 문제가 생길 수 있다.

- 바로 f(n) 함수에서 " n이 커지면 " 커질수록 
  [ ★ 수행 시간이 기하급수적으로 ★ ] 늘어나기 때문
  
- 왜냐하면 ' 동일한 함수가 반복적으로 호출 '되기 때문.
  이미 한 번 계산했지만, [ 계속 호출할 때마다 계산 ]하는 것이여서.

- 즉, f(n)에서 n이 커지면 커질수록 [ 반복해서 호출하는 수가 많아진다. ]

--> 이러한 문제는 ★ 다이나믹 프로그래밍을 사용 ★ 하면 [ 효율적으로 해결 ]가능 
    다만, [ 항상 다이나믹 프로그래밍을 사용 x ]
    
※ 다음 조건을 만족할 때 (다이나믹 프로그래밍)을 사용할 수 있다.
1. 큰 문제를 ★ ' 작은 문제로 나눌 수 ' 있다. ★ 
2. [ 작은 문제에서 구한 정답 ]은 [ ★ 그것을 포함하는 큰 문제에서도 동일 ★  ]하다.
-->  피보나치 수열은 [ 이러한 조건을 만족하는 대표문제 ]다.
     이 문제를 메모이제이션 기법을 사용해서 해결해보자. --> 8-2.py 예제에서 살펴보자.

'''