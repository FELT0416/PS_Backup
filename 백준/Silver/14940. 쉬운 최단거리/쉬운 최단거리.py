import sys
from collections import deque

r, c= map(int, sys.stdin.readline().split())
graph = []
target =False
temp1 = [0]*c
ans = []
visited =[]
for i in range(r):
    temp = list(map(int, sys.stdin.readline().split()))
    if not (target):
        if 2 in temp:
            targetCoord = (temp.index(2),i)
            target=True
    graph.append(temp)

    ans.append(temp1.copy())
    visited.append(temp1.copy())

#print(graph)


dVec = [(-1,0), (0,-1), (1,0), (0,1)]



def bfs(coord):
    visited[coord[1]][coord[0]] = 1
    toVisit = deque()
    toVisit.append(coord)

    while toVisit:
        curX, curY = toVisit.popleft()
        for addX, addY in dVec:
            newX, newY = curX + addX, curY + addY
            if 0 <= newX < c and 0 <= newY < r and graph[newY][newX] == 1 and visited[newY][newX] == 0:
                visited[newY][newX] = 1
                ans[newY][newX] = ans[curY][curX] + 1
                toVisit.append((newX, newY))
        #print(toVisit)

bfs(targetCoord)
#print(targetCoord)
for y in range(r):
    start = True
    for x in range(c):
        if ans[y][x] == 0:
            if graph[y][x]==1:
                ans[y][x] = -1
        if start:
            start = False
            sys.stdout.write(str(ans[y][x]))
        else:
            sys.stdout.write(f" {ans[y][x]}")
    sys.stdout.write("\n")