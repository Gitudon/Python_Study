t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = 0
r = 0
for j in range(m):
    while r < n and a[r] <= b[j]:
        r += 1
    while l < n and a[l] + t < b[j]:
        l += 1
    if l == r:
        print("no")
        break
    l += 1
    if j == m - 1:
        print("yes")
