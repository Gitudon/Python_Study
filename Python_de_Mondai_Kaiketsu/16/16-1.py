n, s = map(int, input().split())
a = list(map(int, input().split()))
answer = "No"
for i in range(0, 1 << n):
    tmp_sum = 0
    for j in range(n):
        if (i >> j) & 1:
            tmp_sum += a[j]
    if tmp_sum == s:
        answer = "Yes"
print(answer)
