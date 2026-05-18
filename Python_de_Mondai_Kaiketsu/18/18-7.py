n = int(input())
answer = 0
for i in range(n):
    for j in range(n - i):
        answer += i * j
print(answer)
