n, m = map(int, input().split())
six_lst = []
one_lst = []
for _ in range(m):
    six, one = map(int, input().split())
    six_lst.append(six)
    one_lst.append(one)
min_six = min(six_lst)
min_one = min(one_lst)

result = min(min_one*n, min_six*(n//6) + min_one*(n%6), min_six*((n + 5)//6))
print(result)