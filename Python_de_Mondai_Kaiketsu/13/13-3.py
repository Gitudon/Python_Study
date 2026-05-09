n = int(input())
a = list(map(int, input().split()))


def min_index(l):
    idx = 0
    for i in range(1, len(l)):
        if l[idx] > l[i]:
            idx = i
    return idx


def second_min_index(l):
    min_idx = min_index(l)
    second_min_index = min_index(l[0:min_idx] + l[min_idx + 1 : len(l)])
    if second_min_index > min_idx:
        second_min_index += 1
    return second_min_index


print(second_min_index(a) + 1)
