n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def min_index(l):
    idx = 0
    for i in range(1, len(l)):
        if l[idx] > l[i]:
            idx = i
    return idx


print(min_index(a) + 1)
print(min_index(b) + 1)
