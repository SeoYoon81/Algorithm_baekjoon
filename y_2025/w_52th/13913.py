 # 숨바꼭질 4 

from collections import deque

# 수빈 위치, 동생 위치
n, k = map(int, input().split())

#bfs로 접근 
parent = [-1 for _ in range(100001)]

parent[n] = n

target = deque([n])

flag = True
while target:
    now_p = target.popleft()
    # k 도착하면 끝
    if now_p == k:
        break
    next_p = [now_p + 1, now_p - 1, now_p * 2]
    for x in next_p:
        # 예외처리
        if x < 0 or x > 100000:
            continue
        if parent[x] != -1:
            continue
        target.append(x)
        parent[x] = now_p

# 이제 경로를 만들어보자 
route = []
node = k
while node != parent[node]:
    next_node = parent[node]
    route.append(node)
    node = next_node

route.append(n)
route.reverse()

print(len(route) - 1)
print(*route)




# 아래는 시간 초과 뜬 풀이

# target = deque([[n]])
# flag = True
# while flag: 
#     now_history = target.popleft()
#     now_point = now_history[-1]
#     next_points = [now_point - 1, now_point + 1, now_point * 2]
#     for x in next_points:
#         # 범위 밖이면 예외
#         if x <0 or x > 100000:
#             continue
#         # 방문 했으면 예외
#         if visit[x]:
#             continue

#         temp_history = now_history + [x]
#         # 동생 잡으면
#         if x == k:
#             answer_history = temp_history
#             flag = False
#             break

#         # 예외 아니면 target에 추가
#         visit[x] = 1
#         target.append(temp_history)
        
# print(len(answer_history) - 1)
# print(*answer_history)