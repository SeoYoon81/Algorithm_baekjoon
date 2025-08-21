import sys
input = sys.stdin.readline

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
set_lst = []
for i in range(n):
    dice = dices[i]
    set_lst.append([{dice[0], dice[5]}, {dice[1], dice[3]}, {dice[2], dice[4]}])
# 0-5, 1-3, 2-4가 같은 줄 
first = dices[0]

max = 0
for i in range(3):
    sum = 0
    