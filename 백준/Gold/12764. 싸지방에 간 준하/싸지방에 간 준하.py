import heapq

n = int(input())

start = []
end = []
empty = [i for i in range(1,n+1)]
ans = []
for _ in range(n):
    temp = tuple(map(int, input().split()))
    heapq.heappush(start, temp)

while start:
    if not end or start[0]<end[0]: # 새로 들어오는 사람 처리
        cur = heapq.heappop(start) # 새로 들어오는 사람
        num = heapq.heappop(empty) # 현재 비어있는 최소 번호
        if len(ans)<num:
            ans.append(1)
        else:
            ans[num-1]+=1
        heapq.heappush(end,(cur[1],num))
    else: # 나가는 사람 처리
        cur = heapq.heappop(end)
        heapq.heappush(empty,cur[1])
print(len(ans))
print(*ans)
