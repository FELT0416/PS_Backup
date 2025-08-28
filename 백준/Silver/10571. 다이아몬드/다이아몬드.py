import sys
input = sys.stdin.readline

rep = int(input())
for _ in range(rep):
    n = int(input())
    dia = [tuple(map(float, input().split())) for _ in range(n)]
    dp=[0]*n
    for ind in range(n-1,-1,-1):
        l = 0
        w, c = dia[ind]
        for ch in range(ind+1,n):
            cw,cc = dia[ch]
            if cw>w and cc<c:
                l = max(l,dp[ch])
        dp[ind] = l+1

    sys.stdout.write(str(max(dp))+'\n')
