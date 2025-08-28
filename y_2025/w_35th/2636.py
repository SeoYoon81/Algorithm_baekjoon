import sys
input = sys.stdin.readline
from collections import deque
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

#입력값 받기 
n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

#전처리
# 1. 0들 visit 처리
target = deque([(0,0)])
border = deque([])
while target:
    i, j = target.popleft()
    for d in range(4):
        n_i, n_j = i + di[d], j + dj[d]
        # 범위 처리
        if n_i < 0 or n_i >= n or n_j < 0 or n_j >= m:
            continue
        # 범위 안에 있다면
        elif box[n_i][n_j] == 0: #공백
            box[n_i][n_j] = -1
            target.append((n_i, n_j))
        elif box[n_i][n_j] == 1:  #치즈
            border.append((n_i, n_j))
# 우선 border을 탐색 대상으로
target = deque(set(border))
ch = len(target)
cnt = 0
while target:
    ch = len(target)
    # 치즈 처리부터 
    for (i, j) in target:
        box[i][j] = -1
    # visit 처리
    new_border = deque([])
    n_target = target
    while n_target:
        n_i, n_j = n_target.popleft()
        for d in range(4):
            new_i, new_j = n_i + di[d], n_j + dj[d]
            # 어차피 경계 아니니까 범위 처리 생략
            if box[new_i][new_j] == 1:
                new_border.append((new_i, new_j))
            elif box[new_i][new_j] == 0:
                box[new_i][new_j] = -1
                n_target.append((new_i, new_j))
    # 다음 턴 위한 데이터셋
    target = deque(set(new_border))
    cnt += 1
print(cnt)
print(ch)
