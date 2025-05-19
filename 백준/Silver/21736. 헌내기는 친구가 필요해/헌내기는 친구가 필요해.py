from collections import deque
h,w = map(int,input().split())

maps = [list(input()) for i in range(h)]

def bfs(coord):
    toVisit = deque([coord])
    ans=0
    maps[coord[1]][coord[0]]="X"
    dirV = [(1,0),(0,1),(-1,0),(0,-1)]
    while toVisit:
        x,y = toVisit.popleft()
        for dx, dy in dirV:
            nx=dx+x
            ny=dy+y
            if 0<=nx<w and 0<=ny<h and maps[ny][nx]!="X":
                if maps[ny][nx]=="P":
                    ans+=1
                maps[ny][nx] = "X"
                toVisit.append((nx,ny))
    return ans

ch=False
for y in range(h):
    for x in range(w):
        if maps[y][x]=="I":
            ch = True
            ans = bfs((x,y))
        if ch:
            break
    if ch:
        break

if ans==0:
    print("TT")
else:
    print(ans)