n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_cnt = [0] * 101
b_cnt = [0] * 101
for i in range(n):
    a_cnt[a[i]] += 1
for i in range(m):
    b_cnt[b[i]] += 1
for i in range(1, 101):
    if (a_cnt > 0) and (b_cnt[i] > 0):
        print(i)
