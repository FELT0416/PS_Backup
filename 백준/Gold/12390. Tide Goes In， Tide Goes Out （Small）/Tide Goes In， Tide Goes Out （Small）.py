import sys
from collections import deque
rep = int(input())
for j in range(1, rep+1):
    h, n, m = map(int,sys.stdin.readline().split())
    ceil = []
    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        ceil.append(temp)
    floor = []
    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        floor.append(temp)


    timeMap = [[float("inf")]*m for _ in range(n)]
    timeMap[0][0]=0
    toVisit = deque([(0,0)])
    dirV = [(1,0),(0,1),(-1,0),(0,-1)]
    while toVisit:
        x, y = toVisit.popleft()
        for dx,dy in dirV:
            nx=x+dx
            ny=y+dy
            if 0<=nx<m and 0<=ny<n and ceil[ny][nx]-floor[ny][nx] >= 50 and ceil[y][x]-floor[ny][nx] >= 50 and ceil[ny][nx]-floor[y][x] >= 50:
                c = ceil[ny][nx]
                f = floor[y][x]
                time = timeMap[y][x]
                w = h - 10 * time
                if c-w <50:
                    wait = (w+50-c)/10
                    time += wait
                    w -= wait*10
                if w != h:
                    if w-f <20:
                        time += 10
                    else:
                        time +=1
                if timeMap[ny][nx] > time:
                    timeMap[ny][nx] = time
                    toVisit.append((nx,ny))
    print(f"Case #{j}: {timeMap[-1][-1]:.1f}")
