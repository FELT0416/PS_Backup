def getPath(start,end):
    startx, starty = start
    endx, endy = end
    path = []
    if startx>endx:
        dir = -1
    else:
        dir = 1
    for x in range(startx, endx+dir,dir):
        path.append((x,starty))
    if starty>endy:
        dir = -1
    else:
        dir = 1
    for y in range(starty+dir, endy+dir,dir):
        path.append((endx, y))
    path.pop() #중복 방지
    return path
        


def solution(points, routes):
    answer = 0
    robotpath = []
    for _ in routes:
        temp=[]
        for i in range(1, len(_)):
            temp.extend(getPath(points[_[i-1]-1], points[_[i]-1]))
        temp.append((points[_[-1]-1][0],points[_[-1]-1][1]))
        robotpath.append(temp)
    time = 0
    for _ in robotpath:
        time = max(time,len(_))
    ind =0
    while ind < time:
        occupied = set()
        alreadychecked = set()
        robotcheck=0
        while robotcheck<len(routes):
            if len(robotpath[robotcheck])<=ind:
                robotcheck+=1
                continue
            coord = robotpath[robotcheck][ind]
            if coord not in occupied:
                occupied.add(coord)
            else:
                if coord not in alreadychecked:
                    answer+=1
                    alreadychecked.add(coord)
            robotcheck+=1
        ind+=1
    return answer