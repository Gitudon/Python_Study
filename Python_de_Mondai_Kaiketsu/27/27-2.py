INF = 10**18
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
dp = [[INF] * (1 << n) for i in range(n)]
dp[0][0] = 0
for j in range(1 << n):
    for i in range(n):
        for k in range(n):
            if (j >> k) & 1 == 0:
                continue
            dp[i][j] = min(dp[i][j], dp[k][j - (1 << k)] + a[k][i])
print(dp[0][(1 << n) - 1])
