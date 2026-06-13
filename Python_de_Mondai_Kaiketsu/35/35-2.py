n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * n for i in range(n)]
answer = 0
for i in range(n):
    prefix_max = a[i]
    for x in range(0, min(i, (i + 1) - k + 1)):
        prefix_max = max(prefix_max, dp[x][i])
    for j in range(i + 1, n):
        if 0 <= j - k <= i:
            prefix_max = max(prefix_max, dp[j - k][i])
        dp[i][j] = prefix_max + a[j]
        answer = max(answer, dp[i][j])
print(answer)
