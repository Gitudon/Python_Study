s = input()
n = len(s)
answer = ""
for i in range(n):
    answer += s[n - 1 - i]
print(answer)
