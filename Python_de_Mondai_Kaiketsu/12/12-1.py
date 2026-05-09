n = int(input())
a, b = map(int, input().split())
c = int(input())
d = [0] * n
for i in range(n):
    d[i] = int(input())
d = sorted(d, reverse=True)
answer = 0
for k in range(n + 1):
    cal_per_doller = (c + sum(d[0:k])) // (a + k * b)
    answer = max(answer, cal_per_doller)
print(answer)
