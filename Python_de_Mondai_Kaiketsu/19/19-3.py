a = list(map(int, input().split()))
for i in range(len(a) - 1):
    min_j = i
    for j in range(i + 1, len(a)):
        if a[min_j] > a[j]:
            min_j = j
    a[i], a[min_j] = a[min_j], a[i]
print(*a)
