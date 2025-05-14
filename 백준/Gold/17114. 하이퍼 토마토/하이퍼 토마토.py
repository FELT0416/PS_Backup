import sys
from collections import deque
size = list(map(int, sys.stdin.readline().split()))
m,n,o,p,q,r,s,t,u,v,w = size

maps =[[[[[[[[[[list(map(int, sys.stdin.readline().split()))
for _ in range(n)]
    for _ in range(o)]
        for _ in range(p)]
            for _ in range(q)]
                for _ in range(r)]
                    for _ in range(s)]
                        for _ in range(t)]
                            for _ in range(u)]
                                for _ in range(v)]
                                    for _ in range(w)]

toVisit = deque()
targets = 0
for w1 in range(w):
    for v1 in range(v):
        for u1 in range(u):
            for t1 in range(t):
                for s1 in range(s):
                    for r1 in range(r):
                        for q1 in range(q):
                            for p1 in range(p):
                                for o1 in range(o):
                                    for n1 in range(n):
                                        for m1 in range(m):
                                            if maps[w1][v1][u1][t1][s1][r1][q1][p1][o1][n1][m1] == 1:
                                                toVisit.append([m1,n1,o1,p1,q1,r1,s1,t1,u1,v1,w1])
                                            elif maps[w1][v1][u1][t1][s1][r1][q1][p1][o1][n1][m1] == 0:
                                                targets+=1 # 안 익은 토마토의 갯수
dir = [-1,1]
ans=0
while toVisit:
    coord = toVisit.popleft()
    a, b, c, d, e, f, g, h, i, j, k = coord
    curTime = maps[k][j][i][h][g][f][e][d][c][b][a]

    for ind, val in enumerate(coord):
        for x in dir:
            if 0<=val+x<size[ind]:
                coord[ind]+= x
                a, b, c, d, e, f, g, h, i, j, k = coord
                if maps[k][j][i][h][g][f][e][d][c][b][a] == 0:
                    maps[k][j][i][h][g][f][e][d][c][b][a] = curTime+1
                    if ans < curTime:
                        ans = curTime
                    toVisit.append([a,b,c,d,e,f,g,h,i,j,k])
                    targets -= 1 # 안 익은 토마토의 갯수 -1
                coord[ind] -= x
if targets==0: # 더 이상 익지 않은 토마토가 없으면 답 출력
    print(ans)
else:
    print(-1)