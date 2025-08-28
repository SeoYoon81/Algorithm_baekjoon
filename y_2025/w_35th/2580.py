# 스도쿠 입력값이랑 빈 값 정보 받기 
sudoku = []
blank = []
for i in range(9):
    now = list(map(int, input().split()))
    for j in range(9):
        if now[j] == 0:
            blank.append((i, j))
    sudoku.append(now)

# set을 만들어보자. 
# i번째 가로줄
row_set_lst = [{0} for _ in range(9)]
# j번째 세로줄
col_set_lst = [{0} for _ in range(9)]
# 3*3 set
sq_set_lst = [[{0} for _ in range(3)] for _ in range(3)]
for i in range(9):
    for j in range(9):
        k = sudoku[i][j]
        row_set_lst[i].add(k)
        col_set_lst[j].add(k)
        sq_set_lst[i//3][j//3].add(k)

# 후보 숫자 찾아볼까 => 이걸 하는게 효율에 좋을지 나쁠지 모르겠다. 
num_in_blank = []
for zero in blank:
    i, j = zero[0], zero[1]
    now_set = []
    for _ in range(1, 10):
        if _ in row_set_lst[i]:
            continue
        if _ in col_set_lst[j]:
            continue
        if _ in sq_set_lst[i//3][j//3]:
            continue
        now_set.append(_)
    num_in_blank.append(now_set)


# 백트래킹 어떻게 하더라......
sol_lst = [0 for _ in range(len(blank))]
def fill_blank(idx):
    # 꽉 찼으면 재귀 끝
    if idx == len(blank):
        return True
    i, j = blank[idx]
    # 각 후보에 대해 실행
    # 공집합이면 return
    if num_in_blank[idx] == []:
        return False
    for k in num_in_blank[idx]:
        # 우선, k가 만족하는지 확인
        if k in row_set_lst[i]:
            continue
        if k in col_set_lst[j]:
            continue
        if k in sq_set_lst[i//3][j//3]:
            continue
        # k가 넣을 수 있는 상태라면
        sol_lst[idx] = k #넣고
        row_set_lst[i].add(k)  #가로줄 
        col_set_lst[j].add(k)  #세로줄
        sq_set_lst[i//3][j//3].add(k)   #3*3
        if fill_blank(idx + 1):
            return True
        # 만족 못하고 나왔으면 원상복귀
        row_set_lst[i].remove(k)
        col_set_lst[j].remove(k)
        sq_set_lst[i//3][j//3].remove(k)

# 실행해볼까
fill_blank(0)
# 빈칸 채우기
for idx in range(len(blank)):
    i, j = blank[idx]
    sudoku[i][j] = sol_lst[idx]

for x in sudoku:
    print(*x)

