n = int(input())
ab = [[0, 0] for i in range(n)]
for i in range(n):
    ab[i] = list(map(int, input().split()))
ab = sorted(ab)
t = [0] * (n + 1)
for i in range(n):
    t[i + 1] = t[i] + ab[i][1]
min_tl_al = 10**18
answer = 0
for r in range(n):
    min_tl_al = min(min_tl_al, t[r] - ab[r][0])
    answer = max(answer, (t[r + 1] - ab[r][0]) - min_tl_al)
print(answer)
