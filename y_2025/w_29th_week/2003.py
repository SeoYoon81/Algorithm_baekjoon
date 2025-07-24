n, m = map(int, input().split())
num_lst = list(map(int, input().split()))
sum_lst = [0]
for i in range(n):
    a = sum_lst[-1]
    b = a + num_lst[i]
    sum_lst.append(b)

cnt = 0
for j in sum_lst:
    if j + m in sum_lst:
        cnt += 1
print(cnt)


'''
4 2
1 1 1 1

3


10 5
1 2 3 4 2 5 3 1 1 2

3
'''
