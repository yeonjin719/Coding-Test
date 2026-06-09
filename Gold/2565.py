n = int(input())
edge = [list(map(int, input().split())) for _ in range(n)]
edge = sorted(edge, key=lambda x: x[0])
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if edge[i][1] > edge[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            print(dp)
print(n - max(dp))