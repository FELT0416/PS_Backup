import heapq, sys
input = sys.stdin.readline

t,n = map(int, input().split())

heap = []
for _ in range(n):
    ids, time, prio = map(int, input().split())
    heapq.heappush(heap, (-prio,ids,time))

for _ in range(t):
    cur = heapq.heappop(heap)
    print(cur[1])
    if cur[2]-1 !=0:
        heapq.heappush(heap,(cur[0]+1,cur[1],cur[2]-1))