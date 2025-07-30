from collections import deque
import sys 
input = sys.stdin.readline
n,m = map(int,input().split())
hx,hy = map(int,input().split())
ex,ey = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

hx-=1
hy-=1
ex-=1
ey-=1
start = ((hx,hy),0)
toVisit = deque()
toVisit.append(start)
visited = [[[-1]*m for _ in range(n)] for w in range(2)]




dirV = [(0,1),(1,0),(0,-1),(-1,0)]
visited[0][hx][hy]=0
while toVisit:
    pos,cnt = toVisit.popleft()
    x,y=pos
    steps = visited[cnt][x][y]
    for dx,dy in dirV:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if maps[nx][ny] == 0:
                if visited[cnt][nx][ny]==-1 or visited[cnt][nx][ny] > steps+1:
                    toVisit.append(((nx,ny),cnt))
                    visited[cnt][nx][ny]=steps+1
            else: # 벽만나면 일단 없애고 다시 탐색
                if cnt ==0:#벽을 한번밖에 못부숨
                    if visited[cnt+1][nx][ny] == -1 or visited[cnt+1][nx][ny] > steps + 1:
                        toVisit.append(((nx, ny), cnt+1))
                        visited[cnt+1][nx][ny] = steps + 1

if  visited[0][ex][ey] ==-1 and visited[1][ex][ey] == -1:
    print(-1)
elif visited[1][ex][ey] ==-1 or visited[1][ex][ey] == -1:
    print(max(visited[0][ex][ey],visited[1][ex][ey]))
else:
    print(min(visited[0][ex][ey],visited[1][ex][ey]))