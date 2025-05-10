"""
평행한면이 3쌍이고, 모든면이 사용되었는지 확인
"""

from collections import deque

for i in range(3):
    ans = True
    maps = []
    for i in range(6):
        temp = list(map(int, input().split()))
        maps.append(temp)
    check=False
    for y in range(6):
        if check:
            break
        for x in range(6):
            if check:
                break
            if maps[y][x] == 1:
                start=(x,y)
                check=True

    neigh = [[-1,-1,-1,-1] for i in range(6)] # 위 아래 좌 우로 설정

    up = (0,-1)
    down = (0,1)
    left = (-1,0)
    right = (1,0)

    dirVec=[up,down,left,right]

    toVisit = deque([start])
    count = -1
    maps[start[1]][start[0]] = count
    while toVisit:
        cur = toVisit.popleft()
        curN = abs(maps[cur[1]][cur[0]])-1

        for nx, ny in dirVec:
            x,y = cur[0]+nx, cur[1]+ny
            if 0<=x<6 and 0<=y<6 and maps[y][x]==1:
                count-=1
                maps[y][x]=count
                newN = abs(count)-1
                toVisit.append((x,y))
                if (nx,ny) == up:
                    neigh[curN][0] = newN
                    neigh[newN][1] = curN
                elif (nx,ny) == down:
                    neigh[curN][1] = newN
                    neigh[newN][0] = curN
                elif (nx,ny) == left:
                    neigh[curN][2] = newN
                    neigh[newN][3] = curN
                elif (nx,ny) == right:
                    neigh[curN][3] = newN
                    neigh[newN][2] = curN
    new=[]
    for i in neigh:
        new.append(i.copy())

    for face in range(6):
        for ne in range(4):
            check=neigh[face][ne]
            if check==-1:
                continue
            if 0<=ne<2:
                if neigh[check][2]!=-1:
                    new[face][2] = neigh[check][2]
                if neigh[check][3]!=-1:
                    new[face][3] = neigh[check][3]
            else:
                if neigh[check][0]!=-1:
                    new[face][0] = neigh[check][0]
                if neigh[check][1]!=-1:
                    new[face][1] = neigh[check][1]

    # 평행한 면 번호 구하기
    neighs = []
    for i in range(6):
        neighs.append([set(),set()])
        for j in range(2):
            if new[i][j]!=-1:
                neighs[i][0].add(new[i][j])
        for j in range(2,4):
            if new[i][j]!=-1:
                neighs[i][1].add(new[i][j])
    perp = []
    for i in neighs:
        for j in i:
            if len(j)==2:
                if j not in perp:
                    perp.append(j)

    for i in perp:
        a, b = i
        for temp in range(2):
            for check in neighs[a][temp]:
                if check in neighs[b][0]:
                    neighs[a][temp] = neighs[a][temp] | neighs[b][0]
                    neighs[b][0] = neighs[a][temp] | neighs[b][0]
                    neighs[a][1-temp] = neighs[a][1-temp] | neighs[b][1]
                    neighs[b][1] = neighs[a][1-temp] | neighs[b][1]
                elif check in neighs[b][1]:
                    neighs[a][temp] = neighs[a][temp] | neighs[b][1]
                    neighs[b][1] = neighs[a][temp] | neighs[b][1]
                    neighs[a][1 - temp] = neighs[a][1 - temp] | neighs[b][0]
                    neighs[b][0] = neighs[a][1 - temp] | neighs[b][0]
    for i in perp:
        for a in i:
            for j in neighs[a]:
                if len(j) == 2 and j not in perp:
                    perp.append(j)
    check = set()
    for i in perp:
        if len(i)!=2:
            ans=False
        for j in i:
            if j in check:
                ans=False
            check.add(j)
    if check!={0,1,2,3,4,5}:
        ans=False
    if ans:
        print("yes")
    else:
        print("no")