r,c = map(int, input().split())
x1,y1,x2,y2 = map(int, input().split())
maps = [list(input()) for _ in range(r)]

toVisit = [(y1-1,x1-1)]
visited = {(y1-1,x1-1)}
dirV = [(1,0),(0,1),(-1,0),(0,-1)]
ans = 0
flag = True
while flag:
    ans+=1
    dead = []
    while toVisit:
        x,y = toVisit.pop()
        for dx,dy in dirV:
            nx,ny = x+dx, y+dy
            if 0<=nx<c and 0<=ny<r and (nx,ny) not in visited:
                if maps[ny][nx]=="1" or maps[ny][nx]=="#":
                    dead.append((nx,ny))
                    visited.add((nx,ny))
                else:
                    toVisit.append((nx,ny))
                    visited.add((nx,ny))
    for cx,cy in dead:
        if maps[cy][cx]=="#":
            flag=False
        maps[cy][cx]="0"
    toVisit = dead
print(ans)