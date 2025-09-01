import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [ 0 for _ in range(n + 1)]
target = deque([])
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for _ in range(1, n + 1):
    if inDegree[_] == 0 :
        target.append(_)

while target:
    now = target.popleft()
    answer.append(now)
    for x in graph[now]:
        inDegree[x] -= 1
        if inDegree[x] == 0:
            target.append(x)

print(*answer)