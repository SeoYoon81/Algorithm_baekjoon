import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weight_lst = []
value_lst = []

for _ in range(n):
    w, v = map(int, input().split())
    weight_lst.append(w)
    value_lst.append(v)

result = 0 

#오랜만에 비트마스킹
for i in range(1<<n):
    now_w = 0
    now_v = 0
    for j in range(n):
        if i & (1<<j):
            now_w += weight_lst[j]
            if now_w > k:
                break
            now_v += value_lst[j]
    if now_w <= k and now_v > result:
        result = now_v

print(result)
