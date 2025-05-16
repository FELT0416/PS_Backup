from collections import deque
n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
for x in range(len(maps[0])):
    for y in range(n):
        if maps[y][x]==9:
            start = (x,y,0)


ans = 0
toVisit = deque([start])
maps[start[1]][start[0]]=0
dirV = [(0,-1),(-1,0),(1,0),(0,1)]
neigh = []
size=2
count = 0
while True:
    visited = set()
    minT = float('inf')
    while toVisit:
        x,y,t = toVisit.popleft()
        for dx, dy in dirV:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(maps[0]) and 0<=ny<n:
                if 0 < maps[ny][nx] < size and (nx,ny) not in visited:
                    visited.add((nx, ny))
                    if t+1<minT:
                        minT = t+1
                        neigh.clear()
                        neigh.append((ny, nx, t + 1))  # 가장 위쪽기준으로 정렬하기 위해 튜플 순서를 바꿈
                    elif t+1==minT:
                        neigh.append((ny, nx, t + 1))
                elif (maps[ny][nx] == 0 or maps[ny][nx] == size) and (nx,ny) not in visited:
                    toVisit.append((nx,ny,t+1))
                    visited.add((nx,ny))
    if not neigh:
        break
    neigh.sort()
    start = neigh[0]
    toVisit.clear()
    toVisit.append((start[1],start[0],0)) # 다시 원래 순서대로 바꾸기
    count+=1
    if count == size:
        size+=1
        count=0
    ans += start[2]
    maps[start[0]][start[1]]=0
    neigh.clear()
print(ans)
