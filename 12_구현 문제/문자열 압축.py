"""
Created on Thu Apr 29 17:38:49 2021

@author: choon
"""

#아래는 -->  M이 (K+1)로 나누어 떨어지지 않는경우 푸는 방법 !!

n, m ,k= map(int, input().split()) # 행, 열

list1 = list(map(int,input().split()))


k2= sorted(list1)  

first = k2[n-1] # 가장 큰 값
second= k2[n-2] # 두번째로 큰 값

result = 0

while True:
    for i in range(k):
        if m ==0 : 
            break
        result += first
        m -= 1
    if m ==0:
        break
    result += second
    m -=1

print(result)
        