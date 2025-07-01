#역순으로 생각하기 
from collections import deque
def solution(board):
    dirV =[(1,0),(-1,0),(0,1),(0,-1)] # 상하좌우
    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            if tile == "R":
                start = (x,y)
                break
    answer = -1
    toCheck=deque()
    visited=set()
    visited.add(start)
    for _ in range(4):
        toCheck.append((start[0],start[1],_,1))
    while toCheck:
        x,y,d,cnt = toCheck.popleft()
        if board[y][x]=="G":
            answer = cnt-1
            break
        
        while 0<=x<len(board[0]) and 0<=y<len(board) and board[y][x]!="D":
            x+=dirV[d][0]
            y+=dirV[d][1]
        x-=dirV[d][0]
        y-=dirV[d][1]
        if (x,y) not in visited:
            visited.add((x,y))
            for _ in range(4):
                if _!=d:
                    temp = (x,y,_,cnt+1)
                    toCheck.append(temp)

    return answer
        