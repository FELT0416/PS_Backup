n,m,h = map(int,input().split())

blocks = [list(map(int,input().split())) for _ in range(n)]

dp = {0:1}
for stu in blocks:
    temp = dp.copy()
    for block in stu:
        for key in temp:
            if key+block in dp:
                dp[key+block]+=temp[key]
                dp[key+block]%=10007
            else:
                dp[key+block]=temp[key]%10007
if h in dp:
    print(dp[h]%10007)
else:
    print(0)