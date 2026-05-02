n = input()
answer = 0
for i in range(len(n)):
    answer += ord(n[i]) - ord("0")
print(answer)
