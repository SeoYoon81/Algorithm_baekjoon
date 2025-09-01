import sys
from collections import deque
input = sys.stdin.readline

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

cnt = 0

while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visit = [ [-1 for _ in range(n)] for _ in range(n)]
    visit[0][0] = matrix[0][0]

    target = deque([(0,0)])
    while target:
        a, b = target.popleft()
        for d in range(4):
            i, j = a + di[d], b + dj[d]
            if i < 0 or i >=n or j<0 or j>=n:
                continue
            if visit[i][j] == -1:
                visit[i][j] = visit[a][b] + matrix[i][j]
                target.append((i,j))
            else:
                if visit[a][b] + matrix[i][j] < visit[i][j]:
                    visit[i][j] = visit[a][b] + matrix[i][j]
                    target.append((i, j))
    print(f'Problem {cnt}: {visit[-1][-1]}')