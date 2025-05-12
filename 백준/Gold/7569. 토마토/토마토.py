import sys
from collections import deque


x, y, z= map(int, sys.stdin.readline().split())

#timeMap이라는 배열로 각 토마토가 익는데 걸리는 시간을 기록
graph = [[[0 for _ in range(x)] for _ in range(y)] for _ in range(z)]
ripePos=[]
timeMap = [[[0 for _ in range(x)] for _ in range(y)] for _ in range(z)]

wallCount=0
for cz in range(z):
    tempz=[]
    for cy in range(y):
        tempStr = list(map(int,sys.stdin.readline().split()))
        for cx in range(x):
            if tempStr[cx] == 1:
                ripePos.append((cx,cy,cz))
            elif tempStr[cx] == -1:
                wallCount+=1
            graph[cz][cy][cx]=tempStr[cx]

#방향벡터
dVec =[(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]


def bfs(ripePose):
    toVisit=deque()
    maxD = 0
    count=0
    for pos in ripePose:
        count+=1
        toVisit.append(pos)
    while toVisit:
        #print(toVisit)
        cx,cy,cz = toVisit.popleft()
        for dx,dy,dz in dVec:
            nx,ny,nz=cx+dx, cy+dy, cz+dz
            if 0<=nx<x and 0<=ny<y and 0<=nz<z and graph[nz][ny][nx]==0:
                if timeMap[nz][ny][nx] == 0 or timeMap[nz][ny][nx]>timeMap[cz][cy][cx]+1:
                    count+=1
                    timeMap[nz][ny][nx] = timeMap[cz][cy][cx] + 1
                    toVisit.append((nx, ny, nz))
                if maxD < timeMap[nz][ny][nx]:
                    maxD = timeMap[nz][ny][nx]

    if count == x*y*z-wallCount:
        return maxD
    else:
        return -1


print(bfs(ripePos))



