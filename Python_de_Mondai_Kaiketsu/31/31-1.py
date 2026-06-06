import heapq

n, m = map(int, input().split())
e = [[] for i in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    e[u].append([v, c])
dist = [10**18] * n
dist[0] = 0
q = []
heapq.heappush(q, [0, 0])
while len(q) != 0:
    d, v = heapq.heappop(q)
    if dist[v] != d:
        continue
    for u, c in e[v]:
        if dist[u] > d + c:
            dist[u] = d + c
            heapq.heappush(q, [d + c, u])
print(dist[n - 1])
