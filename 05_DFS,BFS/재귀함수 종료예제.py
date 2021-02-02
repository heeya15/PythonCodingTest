# -*- coding: utf-8 -*-
"""
p,131
- 재귀함수는 "내부적"으로 [ 스택 자료구조와 동일하다는 것만 기억 !]
  나중에 들어온것이 먼저 나가는 구조.
"""

def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)


