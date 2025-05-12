from collections import deque
import sys

r,c = map(int,sys.stdin.readline().split())

graph=[]
fireDist=[]
jihunDist=[]
FireCheck=False
fire=[]
for y in range(r):
    tempArr=[]
    tempZero=[]
    tempstr=sys.stdin.readline()
    for x in range(c):
        if tempstr[x]=="J":
            jihun = (x,y)
        elif tempstr[x]=="F":
            FireCheck=True
            fire.append((x,y))
        tempArr.append(tempstr[x])
        tempZero.append(0)
    graph.append(tempArr)
    fireDist.append(tempZero.copy())
    jihunDist.append(tempZero.copy())

dVec = [(-1,0),(1,0),(0,-1),(0,1)]


def bfs(coord, Fires=True):
    visited=[]
    for _ in range(r):
        visited.append(tempZero.copy())
    toVisit = deque()
    if Fires:
        for i in coord:
            toVisit.append(i)
            visited[i[1]][i[0]] = 1
    else:
        toVisit.append(coord)
        visited[coord[1]][coord[0]]=1
    while toVisit:
        #print(toVisit)
        curX, curY = toVisit.popleft()
        for dX, dY in dVec:
            newX = curX + dX
            newY = curY + dY
            #print(newX, newY)
            if 0<=newX<c and 0<=newY<r and visited[newY][newX]==0 and graph[newY][newX]!="#":
                if not Fires:
                    if fireDist[newY][newX] <= jihunDist[curY][curX] + 1:
                        if fireDist[newY][newX]!=0:
                            continue
                        elif FireCheck:
                            if (newX, newY) in fire:
                                continue
                visited[newY][newX]=1
                toVisit.append((newX, newY))
                if Fires:
                    fireDist[newY][newX]=fireDist[curY][curX]+1
                else:
                    jihunDist[newY][newX]=jihunDist[curY][curX]+1
if FireCheck:
    #print(fire)
    bfs(fire)
bfs(jihun,False)

minAns=[]
for i in jihunDist:
    if i[0]!=0:
        minAns.append(i[0])
    elif i[c-1]!=0:
        minAns.append(i[c-1])

for j in range(c):
    if jihunDist[0][j]!=0:
        minAns.append(jihunDist[0][j])
    elif jihunDist[r-1][j]!=0:
        minAns.append(jihunDist[r-1][j])

if len(minAns)==0 or jihun[0]==0 or jihun[1]==0:
    if jihun[0]==0 or jihun[1]==0:
        print(1)
    else:
        print("IMPOSSIBLE")
else:

    print(min(minAns)+1)

#print(jihunDist)