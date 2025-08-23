k = 0
while True:
    k += 1
    n = int(input())
    if n == 0:
        break
    # mat - 동굴 정보 
    mat = []
    for _ in range(n):
        lst = list(map(int, input().split()))
        mat.append(lst)
    # visit 첫 줄 만들기
    first_visit = [mat[0][0]]
    for _ in range(1, n):
        a = first_visit[-1] + mat[0][_]
        first_visit.append(a)
    visit = [first_visit] + [[0 for _ in range(n)] for _  in range(n - 1)]
    for i in range(1, n):
        visit[i][0] = visit[i - 1][0] + mat[i][0]
        for j in range(1, n):
            visit[i][j] = min(visit[i - 1][j], visit[i][j - 1]) + mat[i][j]
    
    print(f'Problem {k}: {visit[-1][-1]}')