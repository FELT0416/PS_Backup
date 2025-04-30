import sys
from collections import deque


dVec=[(0,1),(1,0),(-1,0),(0,-1)]


def checkTile(x,y):
    global ans
    tile = maps[y][x]
    if tile == "." or tile in keys:
        maps[y][x] = 1
        toVisit.append((x, y))
    elif tile == "$":
        ans += 1
        maps[y][x] = 1
        toVisit.append((x, y))
    elif tile=="*":
        return
    elif tile.isupper():
        if tile in doors:
            doors[tile].append((x, y))
        else:
            doors[tile] = [(x, y)]
    else:
        keys.add(tile.upper())
        maps[y][x] = 1
        toVisit.append((x, y))



reps = int(sys.stdin.readline())
for _ in range(reps):
    r,c = map(int, sys.stdin.readline().split())
    maps=[]
    for _ in range(r):
        maps.append([*sys.stdin.readline().strip()])
    keys = set()
    k = sys.stdin.readline().strip()
    for i in k:
        keys.add(i.upper())
    ans = 0
    doors = {}  # 현재 열지 못한 문 리스트
    toVisit=deque()


    for i in range(c):
        checkTile(i,0)
        checkTile(i,r-1)
    for i in range(1,r-1):
        checkTile(0,i)
        checkTile(c-1,i)

    while True:
        while toVisit:
            cur= toVisit.popleft()
            for ax, ay in dVec:
                nx, ny = cur[0]+ax, cur[1]+ay

                if 0<=nx<c and 0<=ny<r:
                    tile = maps[ny][nx]
                    if tile=='.': # 빈칸일 경우 탐색
                        toVisit.append((nx,ny))
                        maps[ny][nx] = 1
                    elif tile=='*' or tile==1: # 벽이거나 방문 했을 경우 컨티뉴
                        continue
                    elif tile=='$': # 문서 일 경우 답+1
                        ans+=1
                        maps[ny][nx] = 1
                        toVisit.append((nx, ny))
                    elif tile.isupper(): # 대문자일 경우(문)
                        if tile in keys: # 열쇠를 가지고 있으면 문을 열고 탐색
                            toVisit.append((nx,ny))
                            maps[ny][nx]=1
                        else:
                            if tile in doors: # 잠겨있는 문 딕셔너리에 추가
                                doors[tile].append((nx,ny))
                            else:
                                doors[tile]=[(nx,ny)]
                    else:
                        keys.add(tile.upper()) # 소문자 일 경우(열쇠) 열쇠목록에 추가
                        toVisit.append((nx, ny))
                        maps[ny][nx] = 1

        check=doors.copy()
        for i in check:
            if i in keys:
                for j in doors[i]:
                    toVisit.append(j)
                del doors[i]

        if not toVisit:
            break

    print(ans)
