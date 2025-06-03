n=int(input())
dp = [False]*(n+1)
dp[1]=True
if n>=3:
    dp[3]=True
for _ in range(4,n+1):
    if not dp[_-1] or not dp[_-3]:
        dp[_]=True
if dp[n]:
    print("SK")
else:
    print("CY")
