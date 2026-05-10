n = int(input())


def solve(x):
    if x > n:
        return 0
    res = 1
    last_digit = x % 10
    if last_digit > 0:
        res += solve(x * 10 + last_digit - 1)
    if last_digit < 9:
        res += solve(x * 10 + last_digit + 1)
    return res


answer = 0
for i in range(1, 10):
    answer += solve(i)
print(answer)
