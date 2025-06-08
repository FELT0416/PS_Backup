import sys
r,c,t = map(int,sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

ac = []
for i in range(r):
    if graph[i][0]==-1:
       ac.append((0, i))
dirV = [(0,1),(1,0),(0,-1),(-1,0)]

def move(x,y):
    temp[y][x] += graph[y][x]
    if graph[y][x]==-1:
        return
    for dx, dy in dirV:
        nx, ny = dx+x, dy+y
        if 0<=nx<c and 0<=ny<r and graph[ny][nx]!=-1:
            temp[y][x]-= graph[y][x] // 5
            temp[ny][nx]+= graph[y][x] // 5

for _ in range(t):
    temp = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            move(x,y)
    dir = [2,1,0,3]
    d = 0
    x,y = ac[0]
    y-=1
    while graph[y][x]!=-1:
        dx,dy= dirV[dir[d]]
        nx = x+dx
        ny = y+dy
        if 0<=nx<c and 0<=ny<=ac[0][1]:
            if temp[ny][nx]==-1:
                temp[y][x]=0
            else:
                temp[y][x]=temp[ny][nx]
            x,y=nx,ny
        else:
            d+=1
    dir = [0, 1, 2, 3]
    d = 0
    x,y = ac[1]
    y+=1
    while graph[y][x]!=-1:
        dx,dy= dirV[dir[d]]
        nx = x+dx
        ny = y+dy
        if 0<=nx<c and ac[1][1]<=ny<r:
            if temp[ny][nx]==-1:
                temp[y][x]=0
            else:
                temp[y][x]=temp[ny][nx]
            x,y=nx,ny
        else:
            d+=1
    graph = temp
ans=0
for x in range(c):
    for y in range(r):
        if graph[y][x]!=-1:
            ans+=graph[y][x]
print(ans)