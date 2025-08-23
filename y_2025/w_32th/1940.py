import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
num_lst = list(map(int, input().split()))
num_lst = sorted(num_lst)
i = 0
j = n - 1
cnt = 0
while i < j:
    if num_lst[i] + num_lst[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif num_lst[i] + num_lst[j]<m:
        i += 1
    else:
        j -= 1
print(cnt)