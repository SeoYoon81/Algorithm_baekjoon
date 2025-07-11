## LCS
a_word = input()
b_word = input()

a = len(a_word)
b = len(b_word)
# 같은 문자 위치 기록.
dp = [[0 for _ in range(b + 1)] for _ in range(a + 1)]
for i in range(a):
    for j in range(b):
        if a_word[i] == b_word[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
            
print(dp[a][b])


'''
ACAYKP
CAPCAK

'''