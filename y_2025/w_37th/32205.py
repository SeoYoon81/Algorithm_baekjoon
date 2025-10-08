n = int(input())
line=[]
for _ in range(n):
    now = list(map(int, input().split()))
    line.extend(now)
if len(set(line)) == 3*n:
    print(0)
else:print(1)


