s = input()
answer = ""
for i in range(len(s)):
    if ord("a") <= ord(s[i]) <= ord("z"):
        answer += chr(ord(s[i]) - ord("a") + ord("A"))
    else:
        answer += chr(ord(s[i]) - ord("A") + ord("a"))
print(answer)
