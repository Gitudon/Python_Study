a, b, c, x, y = map(int, input().split())
answer = 10**9
for k in range(max(x, y) + 1):
    i = max(x - k, 0)
    j = max(y - k, 0)
    answer = min(answer, a * i + b * j + c * 2 * k)
print(answer)
