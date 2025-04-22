#dfs로 필요한 건물을 뽑아낸 뒤, dp를 사용해서 시간 구하기
import sys, heapq
from collections import deque

def dfs(n):
    toVisit=[n]
    ans=[]
    while toVisit:
        cur=toVisit.pop()
        if len(req[cur-1])==0:
            ans.append(cur)
            visited.add(cur)
            continue
        visited.add(cur)
        for i in req[cur-1]:
            if i not in visited:
                toVisit.append(i)

    return ans

def dp(n):
    #print("dp")
    complete=True
    for i in unlock[n-1]:
        if dps[i-1]!=-1:
            continue
        tempcheck = True
        #print(unlock[n-1])
        if i not in visited:
            continue
        temp=0
        for j in req[i-1]:
            #print(i,j)
            temp = max(dps[j-1],temp)
            if dps[j-1] == -1:
                tempcheck=False
                complete =False
        if tempcheck:
            dps[i-1]=temp+time[i-1]
            dp(i)
    if not complete:
        return n

rep = int(sys.stdin.readline())
for _ in range(rep):
    n,k = map(int,sys.stdin.readline().split())

    req=[[] for _ in range(n)]
    unlock=[[] for _ in range(n)]
    time = list(map(int, sys.stdin.readline().split()))
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        req[b-1].append(a)
        unlock[a-1].append(b)
    tar = int(sys.stdin.readline())
    visited = set()
    check=deque(dfs(tar))
    dps = [-1]*n
    for i in check:
        dps[i-1]=time[i-1]

    while check:
        cur = check.popleft()
        a = dp(cur)
        if a:
            check.append(a)

    sys.stdout.write(str(dps[tar-1])+'\n')
