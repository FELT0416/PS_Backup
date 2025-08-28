import sys, bisect
input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int,input().split())) for _ in range(n)]

lines.sort()
sub = []
for x,y in lines:
    sub.append(y)


ans = []
for _ in sub:
    ind = bisect.bisect_left(ans,_)
    if ind>=len(ans):
        ans.append(_)
    else:
        ans[ind]=_

print(n-len(ans))