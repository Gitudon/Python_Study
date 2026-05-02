s = input()
n = len(s)
answer = 0
for i in range(n):
    if s[i] == "J":
        answer += 1
print(answer)
