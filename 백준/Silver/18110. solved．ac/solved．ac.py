import sys, heapq
n = int(sys.stdin.readline())

minq = []
maxq = []
sums = 0
for _ in range(n):
    temp = int(sys.stdin.readline())
    heapq.heappush(minq, temp)
    heapq.heappush(maxq, -temp)
    sums += temp

toRemove = int((n*0.15+0.5))
for _ in range(toRemove):
    sums -= heapq.heappop(minq)
    sums += heapq.heappop(maxq)
if n ==0:
    print(0)
else:
    print(int((sums/(n-toRemove*2)+0.5)))
