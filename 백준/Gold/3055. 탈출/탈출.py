from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]
water = []
wmap = [[float("inf")]*m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if maps[y][x]=='D':
            target = (x,y)
        elif maps[y][x]=='S':
            start = (x,y)
        elif maps[y][x]=='*':
            water.append((x,y))
            wmap[y][x]=0



temp = []
dirV = [(1,0),(0,1),(-1,0),(0,-1)]
while water:
    x,y = water.pop()
    for dx, dy in dirV:
        nx = dx+x
        ny = dy+y
        if 0<=nx<m and 0<=ny<n and wmap[ny][nx]==float("inf"):
            if maps[ny][nx]=='.' or maps[ny][nx]=='S':
                wmap[ny][nx]=wmap[y][x]+1
                temp.append((nx,ny))
    if not water:
        water = temp
        temp = []

toVisit = deque([start])
wmap[start[1]][start[0]]=0
while toVisit:
    x,y = toVisit.popleft()
    if (x,y)==target:
        break
    for dx,dy in dirV:
        nx = dx+x
        ny = dy+y
        if 0<=nx<m and 0<=ny<n and (wmap[ny][nx]==-1 or wmap[ny][nx]>abs(wmap[y][x]-1)):
            if maps[ny][nx] == '.' or maps[ny][nx] == 'D':
                toVisit.append((nx,ny))
                wmap[ny][nx]=wmap[y][x]-1

if wmap[target[1]][target[0]]<=0:
    print(abs(wmap[target[1]][target[0]]))
else:
    print("KAKTUS")