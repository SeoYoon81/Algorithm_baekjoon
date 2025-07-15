# 계단 수 
n = int(input())
stair_num = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(n - 1):
    prev_num = stair_num[-1]
    now_num = [prev_num[1]]
    for j in range(1, 9):
        now_num.append(prev_num[j - 1] + prev_num[j + 1])
    now_num.append(prev_num[8])
    stair_num.append(now_num)


print(sum(stair_num[-1]) % 1000000000)
'''
기존 코드 (시간 초과)
import sys
input = sys.stdin.readline

n=int(input())
# i번째 수가 k인 경우
def stair(k, i):
    total=0
    if i==n:
        return 1
    else:
        if k<9:
            total += stair(k+1,i+1)
        if k>0:
            total += stair(k-1, i+1)
    return total
Sum=0
for i in range(1,10):
    Sum+=stair(i,1)
print(Sum%1000000000)


'''