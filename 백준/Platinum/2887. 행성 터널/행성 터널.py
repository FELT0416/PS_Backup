# 인접 간선 목록 구하기
# 프림 > 거리가 0 이면 그 행성의 인접 간선 힙에 추가

import sys, heapq
n = int(sys.stdin.readline())

pos=[]
for _ in range(n):
    x,y,z = map(int, sys.stdin.readline().split())
    pos.append((x,y,z,_))

# 인접 간선 구하기
neigh = [[]for _ in range(n)]
pos.sort(key=lambda a:a[0]) # x축 기준으로 정렬
for i in range(n):
    curP = pos[i]
    if i != n-1:
        nextP=pos[i+1]
        neigh[curP[3]].append((nextP[0]-curP[0],nextP[3]))
        neigh[nextP[3]].append((nextP[0]-curP[0],curP[3]))

pos.sort(key=lambda a:a[1]) # y축 기준으로 정렬
for i in range(n):
    curP = pos[i]
    if i != n-1:
        nextP=pos[i+1]
        neigh[curP[3]].append((nextP[1]-curP[1],nextP[3]))
        neigh[nextP[3]].append((nextP[1]-curP[1],curP[3]))

pos.sort(key=lambda a:a[2]) # z축 기준으로 정렬
for i in range(n):
    curP = pos[i]
    if i != n-1:
        nextP=pos[i+1]
        neigh[curP[3]].append((nextP[2]-curP[2],nextP[3]))
        neigh[nextP[3]].append((nextP[2]-curP[2],curP[3]))

#프림
visited={0}
cur=0
tun = []
ans=0
while len(visited)<n:
    for i in neigh[cur]:
        if i[1] not in visited:
            heapq.heappush(tun, i)
    check = heapq.heappop(tun)
    while check[0]==0 or check[1] in visited:
        if check[0]==0:
            for i in neigh[check[1]]:
                if i[1] not in visited:
                    heapq.heappush(tun, i)
            visited.add(check[1])
            if len(visited) == n:
                break
        check = heapq.heappop(tun)
    ans += check[0]
    visited.add(check[1])
    cur = check[1]

print(ans)
