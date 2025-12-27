#합분해
#중복조합 문제로 접근

n, k = map(int, input().split())

# k개의 바구니에 공 n개를 나누어 넣는 경우의 수
# k H n = (k + n - 1) C (k - 1)
A = 1
B = 1
for i in range(k - 1):
    A *= k + n - 1 - i
    B *= i + 1
print ((A // B) % 1000000000)