"""
지도에 테두리 삽입 - 해당 테두리 = 외부
외부의 한점에서 bfs를 실행하여 접근 가능한 컨테이너 구하기
"""
def edges(maps):
    toVisit = [(0,0)]
    visited = set()
    dirVec = [(1,0),(0,1),(-1,0),(0,-1)]
    edge = []
    while toVisit:
        x, y = toVisit.pop()
        for dx, dy in dirVec:
            nx,ny = dx+x,dy+y
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps) and (nx,ny) not in visited:
                if maps[ny][nx]==0:
                    toVisit.append((nx,ny))
                    visited.add((nx,ny))
                else:
                    edge.append((nx,ny)) 
    return edge
                
                
def solution(storage, requests):
    answer = 0
    maps = [[0]*(len(storage[0])+2)]
    for i in storage:
        temp = [0]
        temp.extend(i)
        temp.append(0)
        maps.append(temp)
    maps.append([0]*(len(storage[0])+2))
    for i in maps:
        print(*i)
                 
    for req in requests:
        if len(req)==1:
            edge = edges(maps)
            for x,y in edge:
                if maps[y][x]==req:
                    answer+=1
                    maps[y][x]=0
        elif len(req)==2:
            for y in range(len(maps)):
                for x in range(len(maps[0])):
                    if maps[y][x]==req[0]:
                        answer+=1
                        maps[y][x]=0
                        
    answer = len(storage[0])*len(storage)-answer
            
    return answer