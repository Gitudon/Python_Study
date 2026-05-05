a = int(input())
d = 2
while a > 1:
    if a % d == 0:
        print(d)
        a //= d
    else:
        d += 1
