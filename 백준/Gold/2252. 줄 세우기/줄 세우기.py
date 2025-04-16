import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())

larger = [[]for _ in range(n)]
smaller = [0 for _ in range(n)]

for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    larger[a-1].append(b)
    smaller[b-1]+=1

toCheck=deque()
for i in range(n):
    if smaller[i] == 0:
        toCheck.append(i+1)
ans=[]

while toCheck:
    cur = toCheck.popleft()
    for i in larger[cur-1]:
        smaller[i-1]-=1
        if smaller[i-1] == 0:
            toCheck.append(i)
    ans.append(cur)
print(*ans)