n, q = map(int, input().split())
s = input()
a = [0] * (n - 1)
for i in range(n - 1):
    if s[i : i + 2] == "AC":
        a[i] = 1
t = [0] * n
for i in range(1, n):
    t[i] = t[i - 1] + a[i - 1]
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(t[r] - t[l])
