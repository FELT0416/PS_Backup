import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split()))for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0]=1

dirV = [(1,0),(0,1)]
for x in range(n):
    for y in range(n):
        if x==n-1 and y==n-1:
            continue
        if y+(maps[y][x])<n:
            dp[y+(maps[y][x])][x]+=dp[y][x]
        if x+(maps[y][x])<n:
            dp[y][x+(maps[y][x])]+=dp[y][x]
print(dp[-1][-1])
        