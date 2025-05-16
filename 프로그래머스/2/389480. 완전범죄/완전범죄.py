def solution(info, n, m):
    comb = []
    bmax = 0
    ans = 10*50
    for i in info:
        bmax+=i[1]
    print(bmax)
    if bmax<m:
        ans=0
    # 각 b의 값에 따른 x의 최솟값을 dp로 구현
    dp = {bmax:0}
    for i in info:
        k = dp.copy()
        for j in k:
            newb = j-i[1]
            newx = k[j]+i[0]
            if newb in dp:
                dp[newb] = min(dp[newb], newx)
            else:
                dp[newb] = newx
            if newb<m and ans>newx and newx<n:
                ans=newx
        print(dp)
    if ans == 10*50:
        ans = -1
    return ans