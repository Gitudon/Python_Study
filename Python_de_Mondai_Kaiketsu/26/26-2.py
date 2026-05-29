n, s = map(int, input().split())
w = [0] * n
v = [0] * n
for i in range(n):
    w[i], v[i] = map(int, input().split())
INF = 10**18
sum_v = sum(v)
dp = [[INF] * (sum_v + 1) for i in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(sum_v + 1):
        if j - v[i] >= 0:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
        else:
            dp[i + 1][j] = dp[i][j]
answer = 0
for i in range(sum_v + 1):
    if dp[n][i] <= s:
        answer = i
print(answer)
