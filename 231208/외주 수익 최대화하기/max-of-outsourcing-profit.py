n = int(input())

dp = [0 for _ in range(n+1)]
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1, -1, -1):
  # print(i)
    if i + arr[i][0] <= n:
        dp[i] = max(dp[i+arr[i][0]] + arr[i][1], dp[i+1])
    else:
        dp[i] = dp[i+1]

    # print(dp)

print(dp[0])