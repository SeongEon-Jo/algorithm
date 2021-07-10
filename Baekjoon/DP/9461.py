n = int(input())
case = []
dp = [0] * 101
for _ in range(n):
    case.append(int(input()))

dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i-5] + dp[i-1]

for x in case:
    print(dp[x])

# input
# 2 
# 6
# 12