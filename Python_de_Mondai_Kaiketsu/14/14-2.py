def solve(x, y):
    if x <= 0 and y <= 0:
        return 0
    return min(solve(x - 1, y - 1) + 1, solve(x // y, y) + 5)


a, b = map(int, input().split())
print(solve(a, b))
