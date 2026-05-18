def my_min(x):
    res = x[0]
    for i in range(len(x)):
        if res > x[i]:
            res = x[i]
    return res


a = list(map(int, input().split()))
print(my_min(a))
