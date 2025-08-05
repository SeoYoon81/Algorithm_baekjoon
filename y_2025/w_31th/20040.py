#사이클 게임
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

#루트 노드 찾기
def find_p(x):
    if parent[x] != x:
        parent[x] = find_p(parent[x])
    return parent[x]

# 두 집합 합치기 + a, b 같은 집합인지 확인 
def union(a, b):
    a = find_p(a)
    b = find_p(b)
    if a != b:
        parent[b] = a
        return False
    return True

# n은 점의 수, m은 입력 수 
n, m = map(int, input().split())
parent = [_ for _ in range(n)]
win = False
for k in range(m):
    x, y = map(int, input().split())
    win = union(x, y)
    if win == True:
        print(k + 1)
        break
if win == False:
    print(0)
