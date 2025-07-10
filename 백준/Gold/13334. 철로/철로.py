import sys, heapq
input = sys.stdin.readline

n = int(input())
start = []
end = []
maxRight = 0
for _ in range(n):
    c,d = map(int, input().split())
    a = min(c,d)
    b = max(c,d)
    heapq.heappush(start,(b,a))
    maxRight = max(maxRight,b)
dist = int(input())
left = 0
right = 0
ans = 0
cur = 0
while start:
    #다음에 확인할 것
    check = heapq.heappop(start)
    right = check[0]
    left = right-dist
    while end and end[0][0]<left:
        heapq.heappop(end)
    if check[1]>=left:
        heapq.heappush(end,(check[1],check[0]))
    cur = len(end)
    ans = max(cur, ans)
print(ans)