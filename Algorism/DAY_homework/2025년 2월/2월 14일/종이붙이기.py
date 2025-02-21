def solve():
    N = int(input())
    dp = [0] * 301
    dp[0] = 1
    dp[10] = 1

    for i in range(20, N + 1, 10):
        dp[i] = dp[i - 10] + 2 * dp[i - 20]

    return dp[N]

T = int(input())
for t in range(1, T + 1):
    result = solve()
    print(f"#{t} {result}")