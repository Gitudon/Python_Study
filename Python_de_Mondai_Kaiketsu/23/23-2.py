r, b = map(int, input().split())
x, y = map(int, input().split())
ok = 0
ng = r + b
while ng - ok > 1:
    m = (ok + ng) // 2
    if r - m >= 0 and b - m >= 0 and (r - m) // (x - 1) + (b - m) // (y - 1) >= m:
        ok = m
    else:
        ng = m
print(ok)
