#  랩실에서 잘 자요

n, m = map(int, input().split())

# 빈 리스트를 만들자. 1은 있는 페이지들 보기 편하게 하기 위함 
book = [1] + [0] * n
pages = list(map(int, input().split()))

# 있는 페이지를 1로
for x in pages:
    book[x] = 1


book += [1] * 3

# 1, 0 수 센 리스트를 만들어보자. 첫 항은 어차피 1에 들어갈까니까 그냥 크게.......
cnt_lst = [3]
for idx in range(1, n + 4):
    if book[idx] == book[idx - 1]:
        cnt_lst[-1] += 1
    else:
        cnt_lst += [1]

# 홀수번째가 2 이하이면 합치는 방식으로...... 
# 이 경우 2k - 1 형식으로 
pay = 0
for i in range(len(cnt_lst)//2):
    if cnt_lst[2 * i] < 3:
        pay += (-5 + 2 * cnt_lst[2 * i])
    pay += (2 * cnt_lst[2 * i + 1] + 5)

print(pay)

'''
10 8
5 7 9 10 3 4 4 3

20

'''