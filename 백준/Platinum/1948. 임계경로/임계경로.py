# 가장 오래걸리는 경로
# 부모의 수만큼 노드까지 걸리는 시간이 비교하면 그때 자식노드 탐색
# 중복 도로 > 부모노드 겹치면 작은거 만큼 빼기
import sys
from collections import deque


input = sys.stdin.readline

n=int(input())
m=int(input())

deg = [0]*n
child = [[]for _ in range(n)]
par = [[]for _ in range(n)]
dp=[[0,0] for _ in range(n)] # 걸리는시간, 갱신된 횟수, 사용된 다리 수
for _ in range(m):
    a,b,c = map(int, input().split())
    child[a-1].append([b,c])
    par[b-1].append([a,c])
    deg[b-1]+=1
root, dest = map(int, input().split())
queue=deque([root])

while queue:
    city=queue.popleft()
    if dp[city-1][1]!=deg[city-1]: # 해당 노드의 시간 갱신이 부모 노드 수 보다 작을 때
        queue.append(city) # 큐 마지막에 다시 삽입
        continue
    for route, time in child[city-1]:
        dp[route-1][1]+=1
        if dp[route - 1][0] < dp[city - 1][0] + time: # 현재 경로가 여태 확인한 가장 오래걸리는 경로보다 오래걸릴 때 갱신
            dp[route - 1][0] = dp[city - 1][0] + time
        if dp[route-1][1]==deg[route-1]:
            queue.append(route)

#목적지부터 다시 bfs로 간선 갯수 체크
queue.append(dest)
count = 0
visited=set()
while queue:
    city = queue.popleft()
    for i in par[city-1]:
        if dp[city-1][0] - i[1] == dp[i[0]-1][0]:
            count+=1
            if i[0] not in visited:
                queue.append(i[0])
                visited.add(i[0])
print(dp[dest-1][0])
print(count)