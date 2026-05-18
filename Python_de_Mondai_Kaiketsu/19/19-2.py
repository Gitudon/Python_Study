a = list(map(int, input().split()))
for i in range(1, len(a)):
    for j in range(len(a) - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a)
