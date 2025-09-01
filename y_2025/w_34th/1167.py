#  트리의 지름
import sys
from collections import deque
input = sys.stdin.readline

# 간선 수
v = int(input())

# leaf 찾기
leaf = []
# 트리 입력 받기
tree = [[] for _ in range(v + 1)]
for i in range(v):
    lines = list(map(int, input().split()))
    num_line = len(lines) // 2 - 1
    if num_line == 1:
        leaf.append(i + 1)
    for k in range(num_line):
        tree[i + 1].append((i + 1, lines[2*k + 1],lines[2*k + 2]))

print(tree)
def find_M(node):
    visit = [1] + [0 for _ in range(v)]
    visit[node] = 1
    length = [0 for _ in range(v + 1)]
    target = deque(tree[node])
    while target:
        s, e, l = target.popleft()
        length[e] = length[s] + l 
        visit[e] = 1
        for line in tree[e]:
            if visit[line[1]] == 0:
                target.append(line)
    return length

first_length = find_M(1)
first_max = max(first_length)
new_s = first_length.index(first_max)
print(max(find_M(new_s)))

