n = int(input())

fruits = list(map(int, input().split())) + [0]
fruit_count = [0 for _ in range(11)]

max_f = 0
i = 0
j = 0

while j <= n:
    #조기 종료 조건
    if max_f > n - i:
        break
    # fruit_count 에서 0 아닌 것 세기
    kind = 0
    for x in fruit_count:
        if x != 0:
            kind += 1
    if kind <= 2:
        max_f = max(max_f, j - i)
        fruit_count[fruits[j]] += 1
        j += 1
    elif kind == 3:
        fruit_count[fruits[i]] -= 1
        i += 1


print(max_f)


'''
5
5 1 1 2 1

3
1 1 1

9
1 2 3 4 5 6 7 8 9
'''