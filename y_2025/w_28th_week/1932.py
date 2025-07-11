import sys
input = sys.stdin.readline

#삼각형 크기
n = int(input())

# 삼각형 입력 - 양 끝 예외처리 귀찮으니까 그냥 앞뒤에 0 붙이자. 
# 자연수라 다행이야
num_tri = []
for _ in range(n):
    num_line = list(map(int, input().split()))
    num_tri.append([0] + num_line + [0])

# 더 큰놈 더해서 숫자 다시 넣는 방식으로
for i in range(1, n):
    for j in range(1, i + 2):
        num_tri[i][j] += max(num_tri[i - 1][j - 1], num_tri[i - 1][j])

print(max(num_tri[-1]))
'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

결과 = 30
'''