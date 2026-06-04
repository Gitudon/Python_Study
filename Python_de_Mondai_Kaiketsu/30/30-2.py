from collections import deque

h, w = map(int, input().split())
s = [""] * h
for i in range(h):
    s[i] = input()
e = [[] for i in range(h * w)]
DI = [0, -1, 0, 1]
DJ = [-1, 0, 1, 0]
dist = [[-1] * w for i in range(h)]
dist[0][0] = 0
q = deque()
q.append([0, 0])


def push(i2, j2, dist2, color_prev):
    if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
        return
    if s[i2][j2] == color_prev:
        return
    if dist[i2][j2] == -1:
        dist[i2][j2] = dist2
        q.append([i2, j2])


while len(q) != 0:
    i, j = q.popleft()
    for k in range(4):
        push(i + DI[k], j + DJ[k], dist[i][j] + 1, s[i][j])
print(dist[h - 1][w - 1])
