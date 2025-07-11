import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        d1 = (r1 + r2) ** 2
        d2 = (r1 - r2) ** 2
        d0 = (x1-x2) ** 2 + (y1 - y2) ** 2
        if d0 == 0 and r1 == r2:
            print(-1)
        elif d0 == d1 or d0 == d2:
            print(1)
        elif d0 < d2 or d0 > d1:
            print(0)
        else: print(2)

