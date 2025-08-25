# 시간초과

# import sys
# input = sys.stdin.readline

# n = int(input())
# num_lst = []
# for _ in range(n):
#     k = int(input())
#     num_lst.append(k)
# num_lst.sort()
# for x in num_lst:
#     print(x)


# 
import sys
input=sys.stdin.readline
n = int(input())
cnt_lst = [0 for _ in range(10001)]

for _ in range(n):
    k = int(input())
    cnt_lst[k] += 1
for k in range(1, 10001):
    if cnt_lst[k] != 0:
        for _ in range(cnt_lst[k]):
            print(k)
