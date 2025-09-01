# 안전영역
import sys
input = sys.stdin.readline
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]

# 최대 최소 찾기 
# 함수 돌릴 범위 정하기 위함
min_l = min([min(land[_]) for _ in range(n)])
max_l = max([max(land[_]) for _ in range(n)])
height = [[] for _ in range(101)]
for i in range(n):
    for j in range(n):
        h = land[i][j]
        height[h].append(n * i + j)
visit = [[0 for _ in range(n)] for _ in range(n)]
# 강수량 k일 때 잠김 여부 만들기 
def rain(k):
    for node in height[k]:
        i, j = node // n, node % n
        visit[i][j] = 1

# visit에 대해 안전지역 수 만들기 
def find_safe(visit):
    copy_visit = [row[:] for row in visit]
    cnt = 0
    for idx in range(n * n):
        i, j = idx // n, idx % n
        if copy_visit[i][j] == 0:
                # 우선 cnt 증가 
            cnt += 1
            target = deque([ i * n + j])
            while target:
                now_idx = target.popleft()
                now_i, now_j = now_idx // n, now_idx % n 
                copy_visit[now_i][now_j] = 1
                for d in range(4):
                    new_i, new_j = now_i + di[d], now_j + dj[d]
                    if new_i not in range(n) or new_j not in range(n):
                        continue
                    if copy_visit[new_i][new_j] == 0:
                        target.append(new_i * n + new_j )
    return cnt

result = 1
for k in range(min_l, max_l):
    rain(k)
    now_safe = find_safe(visit)
    result = max(result, now_safe)

print(result)


