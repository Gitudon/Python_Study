n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())
dpa = [0] * n
dpb = [0] * n
dpc = [0] * n
for i in range(n):
    dpa[i + 1] = max(dpb[i], dpc[i]) + a[i]
    dpb[i + 1] = max(dpc[i], dpa[i]) + b[i]
    dpc[i + 1] = max(dpa[i], dpb[i]) + c[i]
print(max(dpa[n], dpb[n], dpc[n]))
