import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
c = sorted(list(map(int, input().split())))
answer = 0
for i in range(n):
    max_j = bisect.bisect_right(a, b[i])
    min_k = bisect.bisect_left(c, b[i])
    answer += (max_j + 1) * (n - min_k)
print(answer)
