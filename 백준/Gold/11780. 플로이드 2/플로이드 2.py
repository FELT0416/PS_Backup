import sys
input=sys.stdin.readline
n=int(input())
m=int(input())

graph=[[float("inf")]*n for _ in range(n)]
routes = [[[]for _ in range(n)] for _ in range(n)]


for _ in range(m):
    a,b,cost=map(int,input().split())
    if graph[a-1][b-1]>cost:
        graph[a-1][b-1]=cost

for _ in range(n):
    graph[_][_] = 0
    for i in range(n):
        routes[i][_].append(_+1)


for check in range(n):
    for i in range(n):
        base = graph[i][check]
        if base==0:
            continue
        for j in range(n):
            if graph[i][j]>base+graph[check][j]:
                graph[i][j] = base + graph[check][j]
                routes[i][j] = routes[i][check] + routes[check][j]

for i in graph:
    for j in i:
        if j == float("inf"):
            j=0
        sys.stdout.write(str(j)+" ")
    sys.stdout.write("\n")

for i in range(n):
    for j in range(n):
        if graph[i][j]==0 or graph[i][j]==float("inf"):
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(len(routes[i][j])+1))
            sys.stdout.write(' '+str(i+1))
            for k in routes[i][j]:
                sys.stdout.write(' '+str(k))
            sys.stdout.write('\n')
