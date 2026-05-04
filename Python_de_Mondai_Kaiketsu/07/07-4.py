n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_count = [0] * 2001
for i in range(m):
    b_count[b[i]] += 1
answer = 0
for i in range(n):
    if b_count[a[i]] > 0:
        answer += 1
print(answer)
