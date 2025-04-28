import sys, heapq
n = int(sys.stdin.readline())

graph=[]
own = []

for _ in range(n):
    temp=int(sys.stdin.readline())
    own.append(temp)

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)

for _ in range(n):
    graph[_].append(own[_])
own.append(0)
graph.append(own)

visited=[False]*(n+1)
cur = n
visit=1 #방문 노드 수
ans=0
edges=[]
while visit <=n:
    visited[cur]=True
    for i in range(n):
        if graph[cur][i] != 0:
            heapq.heappush(edges,(graph[cur][i],i))
    toVisit=(0,n)
    while visited[toVisit[1]]:
        toVisit = heapq.heappop(edges)
    cur= toVisit[1]
    ans+=toVisit[0]
    visit+=1

print(ans)
