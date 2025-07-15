n = int(input())

bricks = [list(map(int,input().split())) for _ in range(n)] #넓이, 높이, 무게
for _ in range(len(bricks)):
    bricks[_].append(_+1)
bricks.sort()
dp = [[0,0,0,[]]]
for brick in bricks:
    area, h, w, num = brick
    temp = [area,0,w]
    for _ in dp:
        da, dh, dw, mem = _
        temp1 = mem.copy()
        temp1.append(num)
        if da<area and dw<w:
            check = [area, dh+h, w, temp1]
            if dh+h>temp[1]:
                temp = check
    dp.append(temp)

dp.sort(reverse=True, key=lambda x: x[1])
print(len(dp[0][-1]))
for _ in dp[0][-1]:
    print(_)