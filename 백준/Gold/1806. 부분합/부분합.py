import sys
from collections import deque

n, s = map(int, sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))
ans=float("inf")
p1=0
p2=1
check=seq[0]
while p2<n:
    if s <= check:
        check-=seq[p1]
        temp = p2 - p1
        if temp < ans:
            ans = temp
        p1+=1
    if s > check:
        check+=seq[p2]
        p2+=1
while s <= check:
    check -= seq[p1]
    temp = p2 - p1
    if temp < ans:
        ans = temp
    p1 += 1
if ans == float("inf"):
    print(0)
else:
    print(ans)