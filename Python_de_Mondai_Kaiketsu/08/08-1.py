a, b, c = map(int, input().split())
coin = 0
day = 0
while coin < c:
    day += 1
    coin += a
    if day % 7 == 0:
        coin += b
print(day)
