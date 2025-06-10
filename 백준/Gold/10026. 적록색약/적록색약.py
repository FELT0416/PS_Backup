# 적록색약X bfs 먼저 진행
# 노드 방문할 때마다 R,G일때 그래프를 1, G일떄 2으로 변환
from collections import deque
import sys

sizeN = int(input())

graph=[]
for _ in range(sizeN):
    temp=[]
    str = sys.stdin.readline().strip()
    for i in str:
        temp.append(i)
    graph.append(temp)

dVec = [(1,0),(0,1),(-1,0),(0,-1)]

#적록색약Xbfs, 적록색약bfs 나눠서 함수
def bfs(coord):
    if graph[coord[1]][coord[0]] not in ["R", "G", "B"]:
        return 0
    curColor = graph[coord[1]][coord[0]]
    if curColor == "B":
        graph[coord[1]][coord[0]] = 2
    else:
        graph[coord[1]][coord[0]] = 1
    toVisit=deque([coord])
    while toVisit:
        #print(toVisit)
        curX, curY = toVisit.popleft()
        for dx,dy in dVec:
            newX = curX + dx
            newY = curY + dy
            if 0 <= newX < sizeN and 0 <= newY < sizeN and graph[newY][newX] == curColor:
                if curColor == "B":
                    graph[newY][newX] = 2
                else:
                    graph[newY][newX] = 1
                toVisit.append((newX, newY))
    #print("RETURN 1")
    return 1



def bfsRG(coord):
    if graph[coord[1]][coord[0]] not in [1, 2]:
        return 0
    curColor = graph[coord[1]][coord[0]]

    toVisit=deque([coord])
    while toVisit:
        curX, curY = toVisit.popleft()
        for dx,dy in dVec:
            newX = curX + dx
            newY = curY + dy
            if 0 <= newX < sizeN and 0 <= newY < sizeN and graph[newY][newX] == curColor:
                graph[newY][newX] = 0
                toVisit.append((newX, newY))
    return 1


RGBsum=0
for y in range(sizeN):
    for x in range(sizeN):
        RGBsum+=bfs((x,y))

RGsum=0
for y in range(sizeN):
    for x in range(sizeN):
        RGsum+=bfsRG((x,y))


print(f"{RGBsum} {RGsum}")
