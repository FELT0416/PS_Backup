w,h = map(int,input().split())

dp = [[[0,0,0,0] for _ in range(w)] for _ in range(h)] #북,동 / 직전에 방향을 바꾼 갯수

for _ in range(1,w):
    dp[0][_][1]=1
for _ in range(1,h):
    dp[_][0][0]=1


for r in range(1,h):
    for c in range(1,w):
        dp[r][c][1] += dp[r][c-1][1]+dp[r][c-1][3]
        dp[r][c][3] += dp[r][c-1][0]
        dp[r][c][0] += dp[r-1][c][0]+dp[r-1][c][2]
        dp[r][c][2] += dp[r-1][c][1]

        dp[r][c][0]%=100000
        dp[r][c][1]%=100000
        dp[r][c][2]%=100000
        dp[r][c][3]%=100000

print(sum(dp[-1][-1])%100000)