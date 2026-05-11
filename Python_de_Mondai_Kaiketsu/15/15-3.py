from collections import deque

q = deque()
q.append(2)
q.append(5)
q.append(6)
q.popleft()
q.appendleft(0)
q.appendleft(1)
for i in range(len(q)):
    print(q[i])
