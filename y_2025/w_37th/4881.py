while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    # 정지조건 아닐 때 어떻게 할까
    # a, b, 각 경우에 대해 집합으로 접근.
    # 교집합 없으면 answer은 0 
    # 있으면 집합 원소 수랑 교집합 원소 수로 접근
    A, B = a, b
    a_set = {a}
    while True:
        new_a = 0
        while a != 0:
            new_a += (a % 10)**2
            a //= 10
        if new_a in a_set: break
        a_set.add(new_a)
        a = new_a

    b_set = {b}
    while True:
        new_b = 0
        while b != 0:
            new_b += (b % 10) ** 2
            b//=10
        if new_b in b_set: break
        b_set.add(new_b)
        b = new_b
    if len(a_set.intersection(b_set))==0:
        result = 0
    else:  result = len(a_set.union(b_set)) - len(a_set.intersection(b_set)) + 2

    print(A, B, result)