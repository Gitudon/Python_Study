n, k = map(int, input().split())
a = list(map(int, input().split()))
if a[n - 1] < k:
    print(-1)
else:
    l = 0
    r = n - 1
    while l < r:
        m = (l + r) // 2
        if a[m] >= k:
            r = m
        else:
            l = m + 1
    print(l)
