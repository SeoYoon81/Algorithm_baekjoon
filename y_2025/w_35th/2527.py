def find_relation(two_square):
    a_sq = two_square[:4]
    b_sq = two_square[4:]
    a_x, a_y, a_p, a_q = a_sq[0], a_sq[1], a_sq[2], a_sq[3]
    b_x, b_y, b_p, b_q = b_sq[0], b_sq[1], b_sq[2], b_sq[3]
    if a_x > b_x:
        if b_p < a_x:
            result = "d"
        elif b_p == a_x:
            if a_y == b_q or a_q == b_y:
                result = "c"
            elif a_y > b_q or a_q < b_y:
                result = "d"
            else:
                result = "b"
        elif b_p > a_x:
            if b_q < a_y or b_y > a_q:
                result = "d"
            elif b_q == a_y or b_y == a_q:
                result == "b"
            else:
                result = "a"
        
    elif a_x == b_x:
        pass
    elif a_x < b_x:
        pass


for _ in range(4):
    squares = list(map(int, input().split()))