


def solution(land):
    landmap = [[0]*len(land[0]) for _ in range(len(land))]
    dirV = [(-1,0),(1,0),(0,1),(0,-1)]
    def getOil(coord, oilnum):
        toVisit=[coord]
        ans =1
        landmap[coord[1]][coord[0]]=oilnum
        while toVisit:
            cx,cy=toVisit.pop()
            for dx,dy in dirV:
                nx = cx+dx
                ny = cy+dy
                if 0<=nx<len(land[0]) and 0<=ny<len(land):
                    if land[ny][nx]==1 and landmap[ny][nx]==0:
                        landmap[ny][nx]=oilnum
                        toVisit.append((nx,ny))
                        ans+=1  
        return ans
    answer = 0
    count=1
    oildict={0:0}
    for yind, row in enumerate(land):
        for xind, val in enumerate(row):
            if landmap[yind][xind]==0 and land[yind][xind]==1:
                oildict[count]=getOil((xind,yind), count)
                count+=1
    
    for _ in range(len(land[0])):
        oils = set()
        for row in range(len(land)):
            oils.add(landmap[row][_])
        temp =0
        for oil in oils:
            temp+=oildict[oil]
        answer = max(temp,answer)
        
    
    return answer