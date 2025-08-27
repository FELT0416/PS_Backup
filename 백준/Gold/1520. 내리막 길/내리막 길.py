import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]


dp = [[0]*m for _ in range(n)]

dp[0][0]=1

toVisit = [(-maps[0][0],0,0)]
dirV = [(1,0),(0,1),(-1,0),(0,-1)]
while toVisit:
    h,x,y=heapq.heappop(toVisit)
    h*=-1
    for dx,dy in dirV:
        nx=x+dx
        ny=y+dy
        if 0<=nx<m and 0<=ny<n:
            if maps[ny][nx]<h:
                if dp[ny][nx]==0:
                    heapq.heappush(toVisit, (-maps[ny][nx], nx, ny))
                dp[ny][nx]+=dp[y][x]


print(dp[-1][-1])