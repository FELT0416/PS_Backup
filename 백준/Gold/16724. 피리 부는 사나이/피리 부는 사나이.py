# dfs
import sys
r,c = map(int,sys.stdin.readline().split())
maps = [[i for i in sys.stdin.readline().strip()] for _ in range(r)]

ans = 0
count = 1
for x in range(c):
    for y in range(r):
        if maps[y][x]==1:
            continue
        else:
            toVisit = [(x,y)]
            while toVisit:
                cur = toVisit.pop()
                com = maps[cur[1]][cur[0]]
                maps[cur[1]][cur[0]] = count
                if com == "L":
                    nextP = (cur[0] - 1, cur[1])
                elif com == "R":
                    nextP = (cur[0] + 1, cur[1])
                elif com == "D":
                    nextP = (cur[0], cur[1] + 1)
                elif com == "U":
                    nextP = (cur[0], cur[1] - 1)
                else:
                    continue
                check = maps[nextP[1]][nextP[0]]
                if isinstance(check, int):
                    if check == count:
                        ans += 1
                else:
                    toVisit.append(nextP)
            count+=1
print(ans)