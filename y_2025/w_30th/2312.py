n = int(input())
for _ in range(n):
    num = int(input())
    p = 2
    prime_dict = {}
    while p <= num:
        if num % p == 0:
            num /= p 
            if p in prime_dict:
                prime_dict[p] += 1
            else:
                prime_dict[p] = 1
        else:
            p += 1
    for x in prime_dict:
        print(x, prime_dict[x])