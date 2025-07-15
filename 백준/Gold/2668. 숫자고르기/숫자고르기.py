n = int(input())

graph = {}
for _ in range(1,n+1):
    graph[_]= int(input())

answer = set()
visited = set()

for _ in range(1,n+1):
    visited.add(_)
    toVisit = [_]
    path = [_]
    while toVisit:

        cur=toVisit.pop()
        if graph[cur] not in visited:
            path.append(graph[cur])
            visited.add(cur)
            toVisit.append(graph[cur])
        else:
            if graph[cur] in path:
                check = path.index(graph[cur])
                cycle = path[check:]
                for _ in cycle:
                    answer.add(_)
            break

ans = sorted(list(answer))
print(len(ans))
for _ in ans:
    print(_)