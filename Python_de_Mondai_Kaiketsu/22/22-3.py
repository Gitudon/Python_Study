import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
c = sorted(list(map(int, input().split())))
answer = 0
for i in range(n):
    max_j = bisect.bisect_left(a, b[i]) - 1
    min_k = bisect.bisect_right(c, b[i])
    answer += (max_j + 1) * (n - min_k)
print(answer)
