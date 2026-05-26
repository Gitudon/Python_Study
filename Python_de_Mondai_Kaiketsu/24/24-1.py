n = int(input())
ba = [[]] * n
for i in range(n):
    a, b = map(int, input().split())
    ba[i] = [b, a]

ba = sorted(ba)
last_working_day = 0
answer = 0
for i in range(n):
    b, a = ba[i]
    if last_working_day < a:
        last_working_day = b
        answer += 1
print(answer)
