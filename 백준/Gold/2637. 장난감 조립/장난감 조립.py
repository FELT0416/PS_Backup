#부모의 갯수만큼 갱신이 되는지 체크
import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

par=[0]*n
child = [[]for _ in range(n)]
req = [[0,0]for _ in range(n)] # 필요 부품 수 , 갱신 수
req[-1][0]=1

for _ in range(m):
    a, b, cnt = map(int, sys.stdin.readline().split())
    child[a-1].append([b,cnt])
    par[b-1]+=1

ans = []

toCheck = deque([n])
while toCheck:
    cur = toCheck.popleft()
    if req[cur-1][1]!=par[cur-1]: # 부모의 수만큼 갱신이 안됐을 경우
        toCheck.append(cur) # 데크의 끝으로 다시 삽입
        continue
    for i in child[cur-1]:
        ch = i[0]
        cnt = i[1]
        req[ch-1][0]+=cnt*req[cur-1][0]
        req[ch-1][1]+=1
        if req[ch-1][1] == par[ch-1]:
            toCheck.append(ch)
    if len(child[cur-1])==0:
        ans.append([cur, req[cur-1]])


ans.sort()
for i in ans:
    sys.stdout.write(str(i[0])+' '+str(i[1][0])+'\n')