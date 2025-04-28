import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix_A = []
for _ in range(n):
    matrix_A.append(list(map(lambda x: int(x) % 1000, input().split())))
    
def multiple(A, B):
    l = len(A)
    AB = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            AB_ij = 0
            for k in range(l):
                AB_ij += A[i][k] * B[k][j]
            AB[i][j] = AB_ij % 1000
    return AB

def multi_mat(A, k):
    if k == 1:
        return A
    A2 = multi_mat(A, k//2)
    if k % 2 == 1:
        return multiple(multiple(A2, A2), A)
    else: 
        return multiple(A2, A2)

result = multi_mat(matrix_A, b)
for x in result:
    print(*x)
        

'''
2 5
1 2       
3 4      

69 558
337 406

3 3
1 2 3
4 5 6
7 8 9

468 576 684
62 305 548
656 34 412

5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1



512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512


'''