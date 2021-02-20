"""
< 빠르게 입력 받기 > p, 196
- 이진 탐색 문제는 [ 입력 데이터가 많거나 ], [ 탐색 범위가 매우 넓은 편 ]이다.

- 입력 데이터의 개수가 많은 문제에 [ input() 함수를 사용 ]하면 
  동작 속도가 느려 시간 초과로 오답 판정을 받을 수 있다.

- 이처럼 [ 입력 데이터가 많은 문제 ]는 [ sys 라이브러리의 readline() 함수를 이용 ]하면
  시간 초과를 피할수 있다.

※ 때로는 코딩 테스트 출제자가 아예 sys 라이브러리를 사용하기를 권고하는 문장을 
   문제에 적어 놓기도 함.

★ [ sys 라이브러리를 사용할 때는 ] 
  한 줄 입력받고 나서 " rstrip() 함수를 꼭 호출 "해야한다.
  소스코드에 [ readline()으로 입력 ]하면 입력 후 [ 엔터가 줄바꿈 기호로 입력 ]되는데, 
  [ 이 공백 문자를 제거하려면 rstrip() 함수를 사용 ]해야 한다.
  ex) sys.stdin.readline().rstrip()
< 정리 >  
- [ 대량의 데이터를 반복적으로 입력 ]받는 경우 sys.stdin.readline()을 사용하고, 
  입력에 [ 개행을 제거해야 하는 경우 ]는 sys.stdin.readline().strip()보다는
  < input()을 사용하는게 처리 속도면에서 우수 >합니다.

[ 입력 ]
Hello, Coding Test!

"""
# 빠르게 입력받기 --> 시간초과 피할 수 있음
# 7-4.py 한 줄 입력받아 출력하는 소스 코드 .
import sys

# 하나의 문자열 데이터 입력바더기
input_data = sys.stdin.readline().rstrip() # 줄 바꿈을 제거 하기 위해 rstrip() 함수 사용

# 입력받은 문자열 그대로 출력
print(input_data)


