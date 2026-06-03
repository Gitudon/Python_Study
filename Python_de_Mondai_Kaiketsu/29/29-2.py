n, m = map(int, input().split())
a = [0] * m
b = [0] * m
e = [[] for i in range(n)]
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
    e[a[i]].append(b[i])
    e[b[i]].append(a[i])
answer = 0
for i in range(m):
    visited = [0] * n

    def dfs(v):
        global visited
        visited[v] = 1
        for u in e[v]:
            if {v, u} == {a[i], b[i]}:
                continue
            if visited[u] == 0:
                dfs(u)

    dfs(0)
    if sum(visited) < n:
        answer += 1
print(answer)
