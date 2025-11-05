import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

dp = triangle

for level in range(1, n):
    for pos in range(level + 1):
        if pos == 0:  # 맨 왼쪽
            dp[level][pos] = dp[level-1][pos] + triangle[level][pos]
        elif pos == level:  # 맨 오른쪽
            dp[level][pos] = dp[level-1][pos-1] + triangle[level][pos]
        else:  # 가운데 - 최대값 선택
            dp[level][pos] = max(dp[level-1][pos-1], dp[level-1][pos]) + triangle[level][pos]

print(max(dp[n-1]))