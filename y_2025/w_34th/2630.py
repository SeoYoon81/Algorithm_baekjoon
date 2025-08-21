from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
paper = list(list(map(int, input().split())) for _ in range(n))

w = 0
b = 0
remain = deque([paper])
while remain:
    now_p = remain.popleft()
    size = len(now_p)
    color = sum([sum(now_p[i]) for i in range(size)])
    if color == 0:
        w += 1
    elif color == size * size:
        b += 1
    else:
        new_s = size // 2
        next_1 = [now_p[_][:new_s] for _ in range(new_s)]
        next_2 = [now_p[_][new_s:] for _ in range(new_s)]
        next_3 = [now_p[_][:new_s] for _ in range(new_s, size)]
        next_4 = [now_p[_][new_s:] for _ in range(new_s, size)]
        remain.extend([next_1, next_2, next_3, next_4])

print(w)
print(b)
                      

# import sys
# input = sys.stdin.readline

# ### 모두 1인지, 0인지 확인하는 함수
# def check(arr):
#     cnt1 = 0
#     cnt2 = 0
#     for r in range(len(arr)):
#         for c in range(len(arr)):
#             if arr[r][c] == 1:
#                 cnt1 += 1
#             else:
#                 cnt2 += 1
    
#     if cnt1 == (len(arr) ** 2) or cnt2 == (len(arr) ** 2):
#         return True
#     else:
#         return False


# N = int(input())
# color_paper = [list(map(int, input().split())) for _ in range(N)]

# # 개수 파악
# white = 0
# blue = 0


# # 색종이 개수 더하고, 나누는 함수
# def divide(paper):
#     global white, blue

#     if check(paper):

#         if paper[0][0] == 0:
#             white += 1
        
#         else:
#             blue += 1
#         return
    
#     n = len(paper) // 2
#     # 왼쪽 위
#     divide([row[:n] for row in paper[:n]])
    
#     # 오른쪽 위
#     divide([row[n:] for row in paper[:n]])
    
#     # 왼쪽 아래
#     divide([row[:n] for row in paper[n:]])
    
#     # 오른쪽 아래
#     divide([row[n:] for row in paper[n:]])

# divide(color_paper)
# print(white)
# print(blue)

