import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = [int(input())for _ in range(n)]

dp = [-1]*(k+1)
dp[0]=0

for _ in range(1,k+1):
    mins = float("inf")
    for coin in coins:
        if _-coin>=0:
            mins=min(mins,dp[_-coin])
    mins+=1
    dp[_]=mins
if dp[-1]==float("inf"):
    print(-1)
else:
    print(dp[-1])