k, s = map(int, input().split())
answer = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if 0 <= z <= k:
            answer += 1
print(answer)
