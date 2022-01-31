from math import factorial

def combinations_count(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)

n, k = map(int, input().split())
print(combinations_count(n, k))

dp = [[0] * (n + 1) for i in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
print(dp[n][k])