from collections import deque
from itertools import combinations
n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]

# 바이러스 놓을자리
v = {}
walls = 0
for r, row in enumerate(maps):
    for c, col in enumerate(row):
        if col == 2:
            v[(c,r)]=[]
        elif col == 1:
            walls+=1
groups = []
for ox,oy in v.copy():
    group = {(ox,oy)}
    distMap = [[-1]*n for _ in range(n)]
    toVisit = deque([(ox,oy)])
    distMap[oy][ox]=0
    dirV = [(1,0),(-1,0),(0,1),(0,-1)]
    cnt=0
    while toVisit:
        x,y = toVisit.popleft()
        cnt+=1
        for dx,dy in dirV:
            nx,ny= dx+x,dy+y
            if 0<=nx<n and 0<=ny<n and distMap[ny][nx]==-1:
                if maps[ny][nx]==2:
                    group.add((nx,ny))
                    toVisit.append((nx,ny))
                    distMap[ny][nx]=distMap[y][x]+1
                elif maps[ny][nx]==0:
                    toVisit.append((nx, ny))
                    distMap[ny][nx] = distMap[y][x] + 1
    v[(ox,oy)]=distMap
    if group not in groups:
        groups.append([cnt,group])

ans = 10*20
for comb in combinations(v,m):
    cnt = 0
    tempAns = 0
    distMap = [[float("inf")] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for cx,cy in comb:
                if v[(cx,cy)][y][x]!= -1:
                    distMap[y][x]=min(distMap[y][x], v[(cx,cy)][y][x])
            if distMap[y][x]!= float("inf"):
                cnt+=1
                tempAns = max(tempAns,distMap[y][x])

    if cnt+walls == n*n:
        ans = min(ans,tempAns)
if ans !=10*20:
    print(ans)
else:
    print(-1)