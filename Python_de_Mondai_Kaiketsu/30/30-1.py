from collections import deque

h, w = map(int, input().split())
s = [""] * h
for i in range(h):
    s[i] = input()
e = [[] for i in range(h * w)]
DI = [0, -1, 0, 1]
DJ = [-1, 0, 1, 0]
for i in range(h):
    for j in range(w):
        for k in range(4):
            if i + DI[k] < 0 or h <= i + DI[k] or j + DJ[k] < 0 or w <= j + DJ[k]:
                continue
            if s[i][j] != s[i + DI[k]][j + DJ[k]]:
                e[i * w + j].append((i + DI[k]) * w + (j + DJ[k]))
dist = [-1] * (h * w)
dist[0] = 0
q = deque()
q.append(0)
while len(q) != 0:
    v = q.popleft()
    for u in e[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            q.append(u)
print(dist[h * w - 1])
