from collections import deque


def merge_sort(l, r):
    global a
    if r - l == 1:
        return
    m = (l + r) // 2
    merge_sort(l, m)
    merge_sort(m, r)
    q = deque()
    i = l
    j = m
    while i < m and j < r:
        if a[i] < a[j]:
            q.append(a[i])
            i = i + 1
        else:
            q.append(a[j])
            j = j + 1
    while i < m:
        q.append(a[i])
        i = i + 1
    while j < r:
        q.append(a[j])
        j = j + 1
    a[l:r] = q


a = list(map(int, input().split()))
merge_sort(0, len(a))
print(*a)
