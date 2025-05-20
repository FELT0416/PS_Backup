import heapq

n, m = map(int, input().split())
seq = list(map(int, input().split()))
minh = [0]
maxh = [0]
for i in seq:
    if i<0:
        heapq.heappush(minh,i)
    else:
        heapq.heappush(maxh,-i)
ans = -max(abs(minh[0]),abs(maxh[0]))
while minh:
    count=0
    ans-=minh[0]*2
    while minh and count != m:
        heapq.heappop(minh)
        count+=1
while maxh:
    count=0
    ans-=maxh[0]*2
    while maxh and count !=m:
        heapq.heappop(maxh)
        count+=1
print(ans)