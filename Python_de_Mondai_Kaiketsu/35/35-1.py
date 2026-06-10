n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * n for i in range(n)]
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        dp[i][j] = a[i] + a[j]
        for x in range(0, min(i, j - k + 1)):
            dp[i][j] = max(dp[i][j], dp[x][i] + a[j])
        answer = max(answer, dp[i][j])
print(answer)
