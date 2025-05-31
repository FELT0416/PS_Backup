import sys
from collections import deque
n = int(input())
m = int(input())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
x = int(input())

dir = set()

for dist in range(1,x+1):
    for x in range(0,dist):
        y = dist-x
        dir.add((x,y))
        dir.add((x,-y))
        dir.add((-x,y))
        dir.add((-x,-y))
        dir.add((y,x))
        dir.add((y,-x))
        dir.add((-y,x))
        dir.add((-y,-x))

start = deque([(0,0)])
visited = {(0,0)}
safe = matrix[0][0]
ans = False
while start:
    if ans:
        break
    x, y = start.popleft()
    for dx,dy in dir:
        nx,ny = x+dx,y+dy
        if 0<=nx<m and 0<=ny<n:
            if (nx,ny) not in visited and matrix[ny][nx]==safe:
                if nx == m - 1 and ny == n - 1:
                    ans = True
                    break
                start.append((nx,ny))
                visited.add((nx,ny))
if ans:
    print("ALIVE")
else:
    print("DEAD")