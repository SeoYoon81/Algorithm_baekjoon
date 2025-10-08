import sys
input = sys.stdin.readline

v, e = map(int, input().split())
build_dict = {i:[] for i in range(1, v + 1)}
# 도로 입력
for _ in range(e):
    u, v, w = map(int, input().split())
    build_dict[u].append((v, w))
    build_dict[v].append((u, w))

# 맥세권
m, m_len = map(int, input().split())
m_lst = list(map(int, input().split()))
# 스세권
s, s_len = map(int, input().split())
s_lst = list(map(int, input().split()))

def find_min(b_lst, b_len):
    visit = [b_len + 1 for _ in range(v + 1)]
    for x in b_lst:
        visit[x] = 0
    
    pass

