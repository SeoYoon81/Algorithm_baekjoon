import sys
input = sys.stdin.readline

di = [1, 1, 1, 0, -1, -1, -1, 0]
dj = [1, 0, -1, -1, -1, 0, 1, 1]

n, m = map(int, input().split())
word_mat = []
for _ in range(n):
    now = list(input().strip())
    word_mat.append(now)
F_lst = []

for i in range(n):
    for j in range(m):
        now = word_mat[i][j]
        if now == 'F':
            F_lst.append((i, j))

cnt = 0
for node in F_lst:
    now_i, now_j = node
    for d in range(8):
        if now_i + 2 * di[d] < 0 or now_i + 2 * di[d]>=n:
            continue
        if now_j + 2 * dj[d] < 0 or now_j + 2*dj[d] >=m:
            continue
        if (word_mat[now_i  + di[d]][now_j + dj[d]] == 'O') and (word_mat[now_i + 2 * di[d]][now_j + 2*dj[d]] == 'X'):
            cnt += 1

print(cnt)