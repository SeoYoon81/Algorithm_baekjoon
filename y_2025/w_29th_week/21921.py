#21921
n, x = map(int, input().split())
visit_list = list(map(int, input().split()))
cnt_list = [0]
for i in range(n):
    a = cnt_list[-1] + visit_list[i]
    cnt_list.append(a)

print(cnt_list)
history_lst = []
if cnt_list[-1] == 0:
    print('SAD')
else:
    for j in range(n - x + 1):
        history_lst.append(cnt_list[j + x] - cnt_list[j])
    a = max(history_lst)
    print(a)
    print(history_lst.count(a))
'''
5 2
1 4 2 5 1

7
1

7 5
1 1 1 1 1 5 1

9
2


5 3
0 0 0 0 0

SAD


'''