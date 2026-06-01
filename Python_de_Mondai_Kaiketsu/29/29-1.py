import sys

sys.setrecursionlimit(10**9)
n = int(input())
e = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    e[a - 1].append(b - 1)
    e[b - 1].append(a - 1)

visited = [0] * n


def dfs(v):
    global visited
    visited[v] = 1
    print(v + 1, end=" ")
    e[v] = sorted(e[v])
    for u in e[v]:
        if visited[u] == 0:
            dfs(u)
            print(v + 1, end=" ")


dfs(0)
