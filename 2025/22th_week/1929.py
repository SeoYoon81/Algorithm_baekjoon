m, n = map(int, input().split())
p_lst = [0 for _ in range(n + 1)]
p_lst[1] += 1
p = 2
while p * p <= n:
    for i in range(2, n//p + 1):
        p_lst[p * i] += 1
    p += 1

for i in range(m, n + 1):
    if p_lst[i] == 0:
        print(i)
