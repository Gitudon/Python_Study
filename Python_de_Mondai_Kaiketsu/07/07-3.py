n = int(input())
s = input()
a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(n):
    if s[i] == "A":
        a += 1
    elif s[i] == "B":
        b += 1
    elif s[i] == "C":
        c += 1
    elif s[i] == "D":
        d += 1
    elif s[i] == "E":
        e += 1
if a + b + c + d + e >= 3:
    print("Yes")
else:
    print("No")
