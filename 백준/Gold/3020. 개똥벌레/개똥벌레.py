n,h = map(int,input().split())

li = [int(input()) for _ in range(n)]

up = [0]*h
down = [0]*h
for ind, val in enumerate(li):
    if ind%2==0:
        up[val-1]+=1
    else:
        down[h-val-1]+=1

temp = (n+1)//2
for ind, val in enumerate(up):
    temp -= val
    up[ind] = temp

temp = 0
for ind, val in enumerate(down):
    temp += val
    down[ind] = temp

ans = float("inf")
cnt = 0
for _ in range(h):
    temp = up[_]+down[_]
    if ans > temp:
        ans = temp
        cnt=1
    elif ans==temp:
        cnt+=1
print(ans,cnt)