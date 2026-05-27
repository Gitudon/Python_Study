n = int(input())
k = [0] * n
g = 0
for i in range(n):
    a, b = map(int, input().split())
    k[i] = 2 * a + b
    g -= a

k = sorted(k, reverse=True)
for i in range(n):
    g += k[i]
    if g >= 1:
        print(i + 1)
        break
