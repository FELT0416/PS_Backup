import sys, heapq


v, e = map(int, sys.stdin.readline().split())
maps = [[]for _ in range(v)]

for _ in range(e):
    a,b,cost = map(int, sys.stdin.readline().split())
    maps[a-1].append((cost,b))
    maps[b-1].append((cost,a))

# 프림
checked = {1}
edges=[]
cur=1
ans=0
while len(checked)<v:
    for i in maps[cur-1]:
        if i[1] not in checked:
            heapq.heappush(edges, i)
    while cur in checked:
        cost, cur = heapq.heappop(edges)
    ans+=cost
    checked.add(cur)

print(ans)