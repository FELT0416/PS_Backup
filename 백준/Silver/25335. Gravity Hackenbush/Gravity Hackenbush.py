import sys
input = sys.stdin.readline
n,m = map(int,input().split())
for _ in range(n):
    input()
r=0
g=0
b=0
for _ in range(m):
    x, y, z = input().split()
    if z == "R":
        r+=1
    elif z == "G":
        g+=1
    else:
        b+=1

if g %2 ==1:
    r+=1
if r>b:
    print('jhnah917')
else:
    print("jhnan917")
