import sys
from collections import deque

n = int(sys.stdin.readline())
names=sys.stdin.readline().strip().split()
names.sort()
nToid={} # 이름마다 고유 아이디를 부여
idTon={}
for i in range(len(names)):
    nToid[names[i]]=i
    idTon[i]=names[i]
rep=int(sys.stdin.readline())


left = [0]*n
right = [[]for i in range(n)]
left2 = [[]for i in range(n)]
for i in range(rep):
    le1, ri1 = sys.stdin.readline().strip().split()
    le = nToid[le1]
    ri = nToid[ri1]
    right[le].append(ri)
    left[ri]+=1
    left2[ri].append(le)

toCheck=deque()
for i in range(len(left)):
    if left[i]==0:
        toCheck.append(i)
ord=[]
while toCheck:
    cur = toCheck.popleft()
    for i in right[cur]:
        left[i]-=1
        if left[i]==0:
            toCheck.append(i)
    ord.append(cur)

count=0
root=[]
for i in range(len(right)):
    if len(right[i])==0:
        count+=1
        root.append(i)
sys.stdout.write(str(count)+'\n')
for i in root:
    sys.stdout.write(idTon[i]+' ')
sys.stdout.write('\n')


childs=set()
ans=[[]for _ in range(n)]
for i in ord:
    childs.add(i)
    for j in left2[i]:
        if j in childs:
            childs.remove(j)
            ans[i].append(j)

for i in range(n):
    sys.stdout.write(idTon[i]+" "+str(len(ans[i])))
    ans[i].sort()
    for j in ans[i]:
        sys.stdout.write(' '+idTon[j])
    sys.stdout.write('\n')
