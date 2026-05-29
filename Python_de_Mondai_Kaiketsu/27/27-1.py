MOD = 10**9 + 7
h, w = map(int, input().split())
a = [""] * h
for i in range(h):
    a[i] = input()
dp = [[0] * w for i in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]
        if a[i][j] == "#":
            dp[i][j] = 0
        dp[i][j] %= MOD
print(dp[h - 1][w - 1])
