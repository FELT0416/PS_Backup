import sys
input=sys.stdin.readline
r,c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]

def throw(row, dir):
    if dir == 1:
        start = 0
    else:
        start = c-1
    while 0<=start<c:
        if maps[row][start]=="x":
            break
        start+=dir
    if not 0<=start<c:
        return
    check = []
    maps[row][start]="."
    if row <r-1 and maps[row+1][start]=="x":
        check.append((start,row+1))
    if 0<=start+dir<c and maps[row][start+dir]=="x":
        check.append((start+dir,row))
    if row>=1 and maps[row-1][start]=="x":
        check.append((start,row-1))
    clusters = []
    visited = set()
    dirV = [(1,0),(-1,0),(0,1),(0,-1)]
    def getClusters(pos):
        bottom = pos[1]
        toVisit=[pos]
        temp = [[pos[0],pos[1]]]
        visited.add(pos)
        toB = False
        curVisit = set()
        while toVisit:
            x,y = toVisit.pop()
            curVisit.add((x,y))
            for dx,dy in dirV:
                nx = dx+x
                ny = dy+y
                if 0<=nx<c and 0<=ny<r:
                    if maps[ny][nx]=='x' and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        temp.append([nx,ny])
                        toVisit.append((nx,ny))
                        curVisit.add((nx,ny))
                    if (nx,ny) in visited and (nx,ny) not in curVisit:
                        toB = True
                if ny==r:
                    toB = True
            if toB:
                break
        if not toB:
            clusters.append(temp)

    for _ in check:
        getClusters(_)
    if clusters:
        for cluster in clusters:
            for x,y in cluster:
                maps[y][x]='.'
            while True:
                temp = []
                for cx,cy in cluster:
                    cy+=1
                    if cy<r and maps[cy][cx]==".":
                        temp.append((cx,cy))
                    else:
                        break
                if len(temp)== len(cluster):
                    cluster = temp
                else:
                    break
            for x,y in cluster:
                maps[y][x]="x"



rep = int(input())
t = list(map(int,input().split()))
cnt = 0
for cnt, a in enumerate(t):
    if cnt%2==0:
        d = 1
    else:
        d=-1
    throw(r-a,d)

for _ in maps:
    for p in _:
        sys.stdout.write(p)
    sys.stdout.write("\n")
