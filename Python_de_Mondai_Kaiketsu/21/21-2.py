n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
s = [-1] * (n + 1)
for i in range(1, n + 1):
    s[i] = max(s[i - 1], a[i - 1])
t = [-1] * (n + 1)
for i in range(n - 1, -1, -1):
    t[i] = max(t[i + 1], a[i])
for i in range(n):
    print(max(s[i], t[i + 1]))
