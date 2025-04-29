import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maps = [[]for _ in range(n)]
for _ in range(n):
    temp = sys.stdin.readline().strip()
    for i in temp:
        maps[_].append(int(i))

dir = [(0,1),(1,0),(0,-1),(-1,0)]
# 빈공간 영역 구하기
ind = 2
indDict={}
for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            start=(j,i)
            count=1
            toVisit = deque([start])
            maps[start[1]][start[0]]=ind
            while toVisit:
                cur = toVisit.popleft()
                for dx, dy in dir:
                    newx=cur[0]+dx
                    newy=cur[1]+dy

                    if 0<=newx<m and 0<=newy<n and maps[newy][newx]==0:
                        maps[newy][newx] = ind
                        count+=1
                        toVisit.append((newx,newy))
            indDict[ind]= count
            ind+=1
#인접한 영역을 구한뒤, 영역의 넓이(이동가능한 칸) 더하기
for i in range(n):
    for j in range(m):
        ans = 0
        if maps[i][j]==1:
            temp=set()
            for dx, dy in dir:
                cx = j + dx
                cy = i + dy
                if 0 <= cx < m and 0 <= cy < n and maps[cy][cx]!=1:
                    temp.add(maps[cy][cx])
            for k in temp:
                ans+=indDict[k]
            ans+=1
            ans%=10
        sys.stdout.write(str(ans))
    sys.stdout.write('\n')
