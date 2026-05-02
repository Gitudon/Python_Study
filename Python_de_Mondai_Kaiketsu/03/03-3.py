a, b, c = map(int, input().split())
answer = a
if b < answer:
    answer = b
if c < answer:
    answer = c
print(answer)
