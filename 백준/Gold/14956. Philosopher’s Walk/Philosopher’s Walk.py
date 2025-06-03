"""
직접 경로를 구현하여 좌표를 찾는 방법을 시도 하엿으나, 시간 초과.

경로가 몇사분면에 있는지 계속 판별하여 좌표를 구하는 방법으로 새로운 접근

3사분면일때:
4 3
1 2  > (i j) 가 (j i) 가 됨

4사분면일때
2 1
3 4  > i j 가  (대각선만 바뀜)

"""
def getPos(n, len, x=0, y=0, quadrant=[[1,4],[2,3]]):

    if n==2:
        for i in range(2):
            for j in range(2):
                if quadrant[i][j]==len:
                    print(j+1+x,i+1+y)

        return 0
    size = (n//2)**2

    #print(len, size)
    if len %size ==0:
        quad = len // size
    else:
        quad = len // size + 1
    #print(quad)
    newLen = len % size
    if newLen == 0:
        newLen = size

    for py in range(2):
        for px in range(2):
            if quadrant[py][px]==quad:
                curQuad=(px+1,py+1)
    if curQuad==(2,1): #제 4사분면에 위치 (0,0)와(1,1)교체
        x+=n//2
    elif curQuad == (1,2): # 제 2사분면에 위치
        y+=n//2

    elif curQuad == (2,2): # 제 1사분면에 위치
        x+=n//2
        y+=n//2

    if quad == 1:
        quadrant = list(map(list, zip(*quadrant)))
    elif quad == 4:
        quadrant[0][0], quadrant[1][1] = quadrant[1][1], quadrant[0][0]

    #print(n//2, newLen, x, y, quadrant, curQuad, quad)
    getPos(n//2, newLen, x,y,quadrant)
    return 0

xn, xlen = map(int, input().split())
getPos(xn,xlen)