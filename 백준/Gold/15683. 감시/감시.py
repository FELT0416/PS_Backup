def getBest(graph):

    # 카메라 번호별로 좌표와 사각지대가 될 수 없는 칸 갯수 구하기
    r, c = len(graph), len(graph[0])
    posCams=[]
    wallSum=0
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if 0<graph[y][x] <=5:
                posCams.append((graph[y][x], x, y))
                wallSum+=1
            elif graph[y][x] == 6:
                wallSum+=1
    tocheckCells=r*c-wallSum




    dVec = [(1,0),(-1,0),(0,1),(0,-1)] #1번 카메라의 체크 방향

    def checkCam1(pos, dir): #1번카메라의 시야 체크
        forBacktrack=[]
        checkpos = [pos[0]+dir[0], pos[1]+dir[1]]
        #print(checkpos)
        while 0<=checkpos[0]<c and 0<=checkpos[1]<r:
            if graph[checkpos[1]][checkpos[0]]==6:
                return forBacktrack
            elif graph[checkpos[1]][checkpos[0]]==0:
                graph[checkpos[1]][checkpos[0]]="#"
                forBacktrack.append([checkpos[0],checkpos[1]])
            checkpos[0] += dir[0]
            checkpos[1] += dir[1]
        return forBacktrack

    dVec2 = [(1,0),(0,1)]# 2번 전용 방향벡터

    def checkCam(camNum, pos, dir=(0,0)): # 모든카메라의 시선 체크 함수(카메라 번호별로 함수를 만들었다가 수정)
        forBacktrack=[]
        if camNum==1:
            #print(pos, dir)
            forBacktrack = checkCam1(pos,dir)
        elif camNum==2:
            forBacktrack = checkCam1(pos, dir)
            dir = (dir[0] * -1, dir[1] * -1)
            forBacktrack.extend(checkCam1(pos, dir))
        elif camNum==3:
            forBacktrack = checkCam1(pos, dir)
            dir = (dir[1], dir[0] * -1)  ## 90도 회전
            forBacktrack.extend(checkCam1(pos, dir))
        elif camNum==4:
            for i in dVec:
                if i != dir: #특정 방향을 제외한 다른 방향 체크
                    forBacktrack.extend(checkCam1(pos, i))
        elif camNum==5:
            for i in dVec:
                forBacktrack.extend(checkCam1(pos, i))
        return forBacktrack

    def backtrackPath(forBacktrack): # 왔던 경로 다시 지워주기
        for i in forBacktrack:
            graph[i[1]][i[0]]=0


    realAns=[0]

    def backtrack(ind, ans=0):
        if ind == len(posCams):
            if realAns[0] < ans:
                realAns[0] = ans
            return 0
        elif ind > len(posCams):
            return 0
        camNum = posCams[ind][0]
        checkPosition = (posCams[ind][1], posCams[ind][2])


        if camNum==2:
            checkVec = dVec2
        elif camNum==5:
            checkVec = [(0,0)]
        else:
            checkVec = dVec

        for j in checkVec:
            #print(camNum, i)
            newSee=checkCam(camNum, checkPosition, j)
            ans += len(newSee)
            backtrack(ind + 1, ans)
            backtrackPath(newSee)
            ans -= len(newSee)

        return ans
    backtrack(0)
    return tocheckCells-realAns[0]

graph=[]
r, c = map(int, input().split())
for _ in range(r):
    temp=list(map(int, input().split()))
    graph.append(temp)



a=getBest(graph)

print(a)


