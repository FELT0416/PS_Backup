n,m = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 오른쪽에 쓰레기가 있으면 무조건 오른쪽으로
# 오른쪽에 쓰레기가 없으면 한칸 아래로
def clean():
    x=0
    y=0
    cnt=0
    def searchRight(nx,ny,cnt):
        cx=nx
        while cx<m:
            if maps[ny][cx]==1:
                maps[ny][cx]=0
                cnt+=1
                return cx, ny, cnt
            cx+=1
        return nx,ny+1,cnt
    while y!=n:
        x,y,cnt = searchRight(x,y,cnt)
    return cnt
tot = 0
for _ in maps:
    tot+=sum(_)
ans=0
while tot!=0:
    tot-=clean()
    ans+=1

print(ans)
