import sys
input = sys.stdin.readline

def find_p(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

def union(x, y):
    a = find_p(x)
    b = find_p(y)
    if a == b:
        return True
    else:
        parent[b] = a
        return False

n, m = map(int, input().split())
parent = [ _ for _ in range(n) ]
result = False
for k in range(m):
    x, y = map(int, input().split())
    result = union(x, y)
    if result:
        print(k + 1)
        break
    
if not result:
    print(0)

