a = list(map(int, input().split()))
a_cnt = [0] * 100
for i in range(len(a)):
    a_cnt[a[i] - 1] += 1
for i in range(100):
    print(a[i])
