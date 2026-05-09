h, w = map(int, input().split())
a = [[]] * h
for i in range(h):
    a[i] = list(map(int, input().split()))
answer = 1000000000
for i in range(h):
    for j in range(w):
        sum_dist = 0
        for k in range(h):
            for l in range(w):
                if i < k:
                    dist1 = k - i
                else:
                    dist1 = i - k
                if j < l:
                    dist2 = l - j
                else:
                    dist2 = j - l
                if dist1 < dist2:
                    sum_dist += dist1 * a[k][l]
                else:
                    sum_dist += dist2 * a[k][l]
        if sum_dist < answer:
            answer = sum_dist

print(answer)
