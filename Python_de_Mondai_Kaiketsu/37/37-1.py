import bisect
from collections import deque

DX = [0, -1, 0, 1]
DY = [-1, 0, 1, 0]

w, h = map(int, input().split())
n = int(input())
x1 = [0] * n
y1 = [0] * n
x2 = [0] * n
y2 = [0] * n
for i in range(n):
    x1[i], y1[i], x2[i], y2[i] = map(int, input().split())
all_x = sorted(set(x1 + x2 + [0, w]))
all_y = sorted(set(y1 + y2 + [0, h]))
w = len(all_x) - 1
h = len(all_y) - 1
grid = [[0] * (h + 1) for i in range(w + 1)]
for i in range(n):
    x1[i] = bisect.bisect_left(all_x, x1[i])
    x2[i] = bisect.bisect_left(all_x, x2[i])
    y1[i] = bisect.bisect_left(all_y, y1[i])
    y2[i] = bisect.bisect_left(all_y, y2[i])
    grid[x1[i]][y1[i]] += 1
    grid[x1[i]][y2[i]] -= 1
    grid[x2[i]][y1[i]] -= 1
    grid[x2[i]][y2[i]] += 1
for i in range(w):
    for j in range(h):
        if i > 0:
            grid[i][j] += grid[i - 1][j]
        if j > 0:
            grid[i][j] += grid[i][j - 1]
        if (i > 0) and (j > 0):
            grid[i][j] -= grid[i - 1][j - 1]

vis = [[0] * h for i in range(w)]
answer = 0
for i in range(w):
    for j in range(h):
        if (grid[i][j] == 0) and (vis[i][j] == 0):
            answer += 1
            vis[i][j] = 1
            q = deque()
            q.append([i, j])

            def push(x2, y2):
                if not (0 <= x2 < w) or not (0 <= y2 < h):
                    return
                if (grid[x2][y2] > 0) or (vis[x2][y2] == 1):
                    return
                vis[x2][y2] = 1
                q.append([x2, y2])

            while len(q) != 0:
                x, y = q.popleft()
                for k in range(4):
                    push(x + DX[k], y + DY[k])

print(answer)
