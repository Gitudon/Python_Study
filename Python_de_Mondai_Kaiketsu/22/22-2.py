import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
answer = bisect.bisect_left(a, k)
if answer == n:
    print(-1)
else:
    print(answer)
