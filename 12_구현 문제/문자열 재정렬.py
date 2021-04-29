"""
(실전 문제) 럭키 스트레이트 p, 322

- 알파벳 대문자와 숫자 (0~9)로만 구성된 문자열이 입력으로 주어집니다.

- 이때 [ 모든 알파벳을 오름차순으로 정렬 ]하여 이어서 출력한 뒤에, 
  그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

- 예를 들어 K1KA5CB7이 입력으로 들어오면, ABCKK13을 출력합니다.

[ 입력 조건 ]

- 첫째 줄에 하나의 문자열 S가 주어진다. (1 ≤ S의 길이 ≤ 10,000) 
 
[ 출력 조건 ]
- 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

( 입력 예시 )                         ( 출력 예시 1)
K1KA5CB7                               ABCKK13
---------------------------------------------------------
( 입력 예시 )                         ( 출력 예시 2)
AJKDLSI412K4JSJ9D                     ADDIJJJKKLSS20         
"""
# 내가 푼 방법
s= input()

result = []
sum1 = 0
for i in s:  
    if i.isalpha():
        result.append(i)  
        
    else:
        sum1 += int(i) 

result.sort()
if sum1 != 0:
   result.append(str(sum1))
st = ''
for i in result:
    st += i
print(st)



# 책 정답 11-8.py ( p, 516 ) 
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()
print(result)
# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))





