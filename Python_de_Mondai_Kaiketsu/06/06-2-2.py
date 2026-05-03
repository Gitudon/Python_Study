n = int(input())
a = list(map(int, input().split()))
answer = -1
for i in range(n):
    if answer < a[i]:
        answer = a[i]
print(answer)
