import sys
input = sys.stdin.readline

n = int(input())
x=[]
y=[]
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()
dist=0
for _ in range(n//2):
    dist+=x[-_-1]-x[_]+y[-_-1]-y[_]

print(dist)
