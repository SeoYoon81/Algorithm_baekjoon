# 그림

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
