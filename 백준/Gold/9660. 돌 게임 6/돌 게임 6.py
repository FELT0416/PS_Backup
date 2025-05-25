n = int(input())
dp = {0:False, 1:True, 2:False, 3:True, 4:True}

for i in range(5,21):
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i]=True
    else:
        dp[i]=False
if dp[n%7]:
    print("SK")
else:
    print("CY")
