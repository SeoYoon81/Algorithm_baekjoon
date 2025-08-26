# 햄버거 분배

n, k = map(int, input().split())
table = list(input())
h_lst = [0 for _ in range(n)]
p_lst = [0 for _ in range(n)]
for i in range(n):
    if table[i] == "H":
        h_lst[i] = 1
    else:
        p_lst[i] = 1
cnt = 0
for i in range(n):
    if p_lst[i] == 0:
        continue
    for t in range(-k, k + 1):
        if i + t < 0 or i + t >=n:
            continue
        if h_lst[i + t] == 1:
            h_lst[i + t] = 0
            cnt += 1
            break
print(cnt)