from collections import deque

s = []
q = deque()

s.append(1)
s.append(2)
s.append(3)
print(s.pop(), s.pop(), s.pop())

q.append(1)
q.append(2)
q.append(3)
print(q.popleft(), q.popleft(), q.popleft())