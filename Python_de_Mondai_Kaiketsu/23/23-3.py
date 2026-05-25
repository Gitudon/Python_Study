n = int(input())
h = [0] * n
s = [0] * n
for i in range(n):
    h[i], s[i] = map(int, input().split())
ok = 10**14
ng = -1
while ok - ng > 1:
    m = (ok + ng) // 2
    t = [0] * n
    for i in range(n):
        if m < h[i]:
            t[i] = -1
        else:
            t[i] = (m - h[i]) // s[i]
    t = sorted(t)
    is_ok = True
    for i in range(n):
        if t[i] < i:
            is_ok = 0
    if is_ok == 1:
        ok = m
    else:
        ng = m
print(ok)
