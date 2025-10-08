from collections import deque

n = int(input())
paper_lst = [0] + list(map(int, input().split()))
# 남아있는 풍선
ballons = [_ for _ in range(1, n + 1)]
result = []
while ballons:
    now_ballon = ballons[0]
    result.append(now_ballon)
    next_idx = (ballons[now_ballon]+len(ballons)) % len(ballons)
    ballons = ballons[next_idx:] + ballons[1:next_idx ] 
    print('paper', next_idx)
    print(ballons)

print(*result)
