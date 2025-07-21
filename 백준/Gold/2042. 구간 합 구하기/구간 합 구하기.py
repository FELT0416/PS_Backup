import sys
sys.setrecursionlimit(10*100)
input=sys.stdin.readline

n,m,k = map(int,input().split())

seq = [int(input()) for _ in range(n)]

length = 1
while length < n:
    length*=2
l = length*2
seg = [0]*l
for ind, val in enumerate(seq):
    seg[length+ind]=val

for ind in range(length-1,0,-1):
    seg[ind] = seg[ind*2]+seg[ind*2+1]

def find(s,e,n,ts,te):
    if te<s or e<ts:
        return 0
    if ts<=s<=e<=te:
        return seg[n]
    else:
        mid = (s+e)//2
        return find(s,mid,n*2,ts,te)+find(mid+1,e,n*2+1,ts,te)

def update(n, v):
    start = length+n-1
    diff = v-seg[start]
    while start>=1:
        seg[start]+=diff
        start//=2
for _ in range(k+m):
    a,b,c = map(int,input().split())
    if a == 1:
        update(b,c)
    else:
        sys.stdout.write(str(find(1,length,1,b,c))+'\n')