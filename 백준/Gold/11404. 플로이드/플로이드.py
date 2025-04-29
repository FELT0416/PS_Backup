import sys
input=sys.stdin.readline
n=int(input())
m=int(input())

graph=[[float("inf")]*n for _ in range(n)]

for _ in range(m):
    a,b,cost=map(int,input().split())
    if graph[a-1][b-1]>cost:
        graph[a-1][b-1]=cost
for _ in range(n):
    graph[_][_] = 0

for check in range(n):
    for i in range(n):
        base = graph[i][check]
        for j in range(n):
            if graph[i][j]>base+graph[check][j]:
                graph[i][j] = base + graph[check][j]

for i in graph:
    for j in i:
        if j == float("inf"):
            j=0
        sys.stdout.write(str(j)+" ")
    sys.stdout.write("\n")
