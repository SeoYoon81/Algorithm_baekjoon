### 히오스 프로그래머

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lv_lst = []
for _ in range(n):
    lv_lst.append(int(input()))

lv_lst.sort()
t = lv_lst[0]

idx = 1
while k >= idx:
    # print('k', k)
    # print('idx', idx)
    # print('t', t)
    if idx == n:
        t += k // n
        k = 0

    elif lv_lst[idx] == t:
        idx += 1
    else:
        k -= idx
        t += 1

print(t)
