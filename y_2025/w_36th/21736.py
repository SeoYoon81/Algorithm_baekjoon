import sys
input = sys.stdin.readline
from collections import deque

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            a, b = i, j
visit[a][b] = 1
target = deque([(a, b)])
cnt = 0
while target:
    now_i, now_j = target.popleft()
    if campus[now_i][now_j] == 'P':
        cnt += 1
    for d in range(4):
        new_i, new_j = now_i + di[d], now_j + dj[d]
        if new_i not in range(n) or new_j not in range(m):
            continue
        if campus[new_i][new_j] == 'X':
            continue
        if visit[new_i][new_j] == 0:
            target.append((new_i, new_j))
            visit[new_i][new_j] = 1

if cnt == 0:
    result = 'TT'
else: result = cnt
print(result)