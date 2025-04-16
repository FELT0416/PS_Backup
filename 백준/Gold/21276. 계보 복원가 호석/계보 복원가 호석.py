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

# 그래프 표현하기
left = [0]*n # 연결된 자식 수 (len(left2)값과 동일하지만 이후에 수정이 필요하므로 따로 분리)
right = [[]for i in range(n)] # 연결된 조상
left2 = [[]for i in range(n)] # 연결된 자식
for i in range(rep):
    le1, ri1 = sys.stdin.readline().strip().split()
    le = nToid[le1]
    ri = nToid[ri1]
    right[le].append(ri)
    left[ri]+=1
    left2[ri].append(le)

toCheck=deque()
for i in range(len(left)): # 자식이 없는 노드들을 전부 큐로 넣기
    if left[i]==0:
        toCheck.append(i)
ord=[]
while toCheck:
    cur = toCheck.popleft()
    for i in right[cur]: # 해당 노드의 조상들 체크 조상이 다른 자식이 더 이상 없으면 큐에 삽입
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


childs=set() # 위상 정렬을 토대로 조상의 직계 자식을 구하기
ans=[[]for _ in range(n)]
for i in ord:
    childs.add(i)
    for j in left2[i]:
        if j in childs:
            childs.remove(j)
            ans[i].append(j)

#요구 출력대로 출력

for i in range(n):
    sys.stdout.write(idTon[i]+" "+str(len(ans[i])))
    ans[i].sort()
    for j in ans[i]:
        sys.stdout.write(' '+idTon[j])
    sys.stdout.write('\n')
