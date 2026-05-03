n = int(input())
a = list(map(int, input().split()))
answer = 0
for i in range(n):
    answer += a[i]
print(answer)
