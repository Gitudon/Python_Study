import sys

input = sys.stdin.readline
n, q, s, t = map(int, input().split())
a = [0] * (n + 1)
for i in range(n + 1):
    a[i] = int(input())
b = [0] * n
for i in range(n):
    b[i] = a[i + 1] - a[i]
answer = 0


def apply(i):
    global answer
    if b[i] > 0:
        answer += -s * b[i]
    else:
        answer += -t * b[i]


def cancel(i):
    global answer
    if b[i] > 0:
        answer -= -s * b[i]
    else:
        answer -= -t * b[i]


for i in range(n):
    apply(i)
for i in range(q):
    l, r, x = map(int, input().split())
    cancel(l - 1)
    b[l - 1] += x
    apply(l - 1)
    if r < n:
        cancel(r)
        b[r] -= x
        apply(r)
    print(answer)
