a = int(input())
i = 1
while i * i <= a:
    a -= i * i
    i += 1
print(i)
