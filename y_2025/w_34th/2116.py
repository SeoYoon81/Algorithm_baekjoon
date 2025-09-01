import sys
input = sys.stdin.readline

dice_dict = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}
n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]


max_sum = 0
for i in range(6):
    sum = 0
    bottom = dices[0][i]
    for k in range(n):
        now_dice = dices[k]
        bottom_idx = now_dice.index(bottom)
        top_idx = dice_dict[bottom_idx]
        new_dice = [now_dice[i] for i in range(6) if i not in [bottom_idx, top_idx]]
        sum += max(new_dice)
        bottom = now_dice[top_idx]
    max_sum = max(max_sum, sum)
print(max_sum)