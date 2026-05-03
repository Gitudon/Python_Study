a = list(map(int, input().split()))
a_cnt = [0] * 101
for i in range(len(a)):
    a_cnt[a[i]] += 1
for i in range(1, 101):
    print(a[i])
