# 오큰수
n = int(input())
ori_lst = list(map(int, input().split()))
# 2중 for문 사용 시간초과
# big_mat = [-1 for _ in range(n)]
# for i in range(n):
#     for j in range(i, n):
#         if ori_lst[i] < ori_lst[j]:
#             big_mat[i] = ori_lst[j]
#             break
# print(*big_mat)

result = [-1 for _ in range(n)]
stack = []
for i in range(n):
    while stack and ori_lst[stack[-1]] < ori_lst[i]:
        result[stack[-1]] = ori_lst[i]
        stack.pop()
    stack.append(i)
print(* result)

'''
4
3 5 2 7

5 7 7 -1

4
9 5 4 8

-1 8 8 -1

'''