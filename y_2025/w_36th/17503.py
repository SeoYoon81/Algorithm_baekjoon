import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
beer_lst = []
for _ in range(k):
    like, alchol = map(int, input().split())
    beer_lst.append((alchol, like))

#  -1 판단
beer_lst.sort(key=lambda x: (x[0], x[1]), reverse=True)
maximum = sum([beer[1] for beer in beer_lst[:n]])
if maximum < m: result = -1
else: #간수치 설정 가능할 때
    beer_lst.sort(key=lambda x: (x[0], -x[1]))
    # ???? 이건 아닌것같은디 