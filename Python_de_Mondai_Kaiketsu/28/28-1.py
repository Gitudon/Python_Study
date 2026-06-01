n, m = map(int, input().split())
a = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)
