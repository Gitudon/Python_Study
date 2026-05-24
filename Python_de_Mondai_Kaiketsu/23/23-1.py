n, k = map(int, input().split())
a = list(map(int, input().split()))
ok = n
ng = -1
while ok - ng > 1:
    m = (ok + ng) // 2
    if a[m] >= k:
        ok = m
    else:
        ng = m
if ok == n:
    print(-1)
else:
    print(ok)
