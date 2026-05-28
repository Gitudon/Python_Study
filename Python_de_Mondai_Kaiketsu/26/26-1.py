n, s = map(int, input().split())
w = [0] * n
v = [0] * n
for i in range(n):
    w[i], v[i] = map(int, input().split())
INF = 10**18
dp = [[-INF] * (s + 1) for _ in range(n + 1)]
dp[0][s] = 0
for i in range(n):
    for j in range(s + 1):
        if j + w[i] <= s:
            dp[i + 1][j] = max(dp[i][j], dp[i][j + w[i]] + v[i])
        else:
            dp[i + 1][j] = dp[i][j]
print(max(dp[n]))
