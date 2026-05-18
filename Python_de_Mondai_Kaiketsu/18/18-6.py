n, k = map(int, input().split())
answer = 0
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            break
        if i * j == k:
            answer += 1
print(answer)
