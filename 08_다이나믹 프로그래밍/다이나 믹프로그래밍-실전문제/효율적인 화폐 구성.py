"""
(실전 문제) 효율적인 화폐 구성 p, 226

- [ N가지 종류의 화폐 ]가 있다.
  이 화폐들의 [ 개수를 ** 최소한으로 이용 ** ]해서 그 가치의 [ 합이 M원이 되도록 하려고 ] 한다.
- 이때 각 화폐는 몇 개라도 사용할 수 있으며, 
 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.

ex)예를 들어 [ 2원, 3원 단위의 화폐가 있을 때 ]는 [ 15원을 만들기 위해 ] 
   [ 3원을 5개 사용하는 것 ]이 [ 가장 최소한의 화폐 개수 ]이다.

------------------------------------------------------------------------------
[ 입력 조건 ]

- [ 첫째 줄 ]에 N, M이 주어진다. (1 <= N <= 100 , 1 <= M <= 10,000)  
- [ 이후 N개의 줄 ]에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.

[ 출력 조건 ]

- 첫째 줄에 [ M원을 만들기 위한 ] < 최소한의 > 화폐 개수를 출력한다.

- 화폐를 만들기 [ 불가능할 때는 "-1을" 출력 ]한다.
[ 입력 ]                     [ 출력 ]
2 15
2                               5 (최소 3원을 5개 사용한 경우 15원을 만듬.)
3

------------------------------------------------------------------------------

3  4
3                               -1 (불가능 한경우)
5
7                             
   
※ dp 테이블을 특정 크기만큼 만들어주고, 점화식에 맞게 하나씩 채워주면 된다.
   즉, 점화식을 찾는게 dp에서 가장큰 핵심이라고 할 수 있다.
   < 조건 >
# 각 인덱스에 해당하는 값으로 10,001을 설정한다.
# 10,001은 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 의미이다.
# [ M의 최대 크기가 10,000이므로 ] 불가능 한 수로 10,001이라는 값을 설정.   
"""
# 8-8.py 책 정답 p,228
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[ j - array[i] ] + 1)  # array[i] = 각 화폐의 단위이다.
            print(j, d[j])
# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print("최종 답:"+str(d[m]))

