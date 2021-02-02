from collections import deque
"""
p, 129
큐(Queue) 구현을 위해 [ deque 라이브러리 사용 ]
- Deque(데크)는 double-ended queue 의 줄임말로, 
 앞과 뒤에서 즉, [ 양방향에서 ] 데이터를 처리할 수 있는 
 queue형 자료구조를 의미한다. 
- deque는 리스트 처럼 중간 내용을 수정하거나 삭제 가능.

 appendleft(x)는 
--> 왼쪽 즉, 앞쪽에서 x를 추가(삽입)해주는 메소드

 append(x)
- 큐에 오른쪽에 원소를 넣을때 사용한다.

 popleft()

큐에 원소 왼쪽을 제거할 때 사용한다.

※ deque 객체를 [ 리스트 자료형으로 변경 ]하고자 한다면
- list(Queue)를 하면 리스트 자료형이 반환된다.
"""

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
Queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
Queue.append(5) # 덱의 오른쪽에 삽입.
Queue.append(2)
Queue.append(3)
Queue.append(7)
Queue.popleft() # 제일 왼쪽 값을 꺼낸다. -- 5
Queue.append(1)
Queue.append(4)
Queue.popleft() # 제일 왼쪽 값을 꺼낸다. -- 2
#Queue.pop()     # 제일 오른쪽 값을 꺼낸다. -- 4

print(Queue) # 먼저 들어온 순서대로 출력
Queue.reverse() # 다음 출력을 위해 [ 역순 ]으로 바꾸기 
print(Queue) # 나중에 들어온 원소부터 출력