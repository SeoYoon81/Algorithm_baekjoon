# N과 M (3)
# DFS로 접근
# 근데 DFS 어떻게 했더라... 생각이 안 나 


n, m = map(int, input().split())

# 리스트 길이가 m 되면 출력하는 형태로....
def dfs(a, b, lst):
    if len(lst) == b:
        print(*lst)
        return
    for i in range(1, a + 1):
        lst.append(i)
        dfs(a, b, lst)
        # lst 원상복귀
        lst.pop()

dfs(n, m, [])