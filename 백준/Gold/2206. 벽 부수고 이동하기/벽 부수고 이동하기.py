from collections import deque
import sys
input = sys.stdin.readline
n,m= map(int,input().split())
k=1
maps = [[int(i) for i in input().strip()] for _ in range(n)]
start = ((0,0),0)
toVisit = deque()
toVisit.append(start)
visited = [[[-1]*m for _ in range(n)] for w in range(k+1)]



dirV = [(0,1),(1,0),(0,-1),(-1,0)]
visited[0][0][0]=1
while toVisit:
    pos,cnt = toVisit.popleft()
    x,y=pos
    steps = visited[cnt][x][y]
    for dx,dy in dirV:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if maps[nx][ny] == 0:
                if visited[cnt][nx][ny]==-1:
                    toVisit.append(((nx,ny),cnt))
                    visited[cnt][nx][ny]=steps+1
            else: # 벽만나면 일단 없애고 다시 탐색
                if cnt <k:#벽을 한번밖에 못부숨
                    if visited[cnt+1][nx][ny] == -1:
                        toVisit.append(((nx, ny), cnt+1))
                        visited[cnt+1][nx][ny] = steps + 1

ans = []
for _ in range(k+1):
    if visited[_][-1][-1]!=-1:
        ans.append(visited[_][-1][-1])
if len(ans)!=0:
    print(min(ans))
else:
    print(-1)