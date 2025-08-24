import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int,input().split()))
m = int(input())


start = 1
while start<n:
    start<<=1
length = start*2
seg = [0]*length
for ind, val in enumerate(seq):
    seg[start+ind]= val
for _ in range(start-1,0,-1):
    seg[_]= seg[_*2]+seg[_*2+1]
lazy = [0]*length

def prop(s,e,n):
    if n<start:
        lazy[2*n]+=lazy[n]
        lazy[2*n+1]+=lazy[n]
    seg[n]+=lazy[n]*(e-s+1)
    lazy[n]=0

def update(s,e,n,ts,te,v):
    prop(s,e,n)
    if ts>e or te<s:
        return
    elif ts<=s<=e<=te:
        lazy[n]+=v
        prop(s,e,n)
    else:
        mid = (s+e)//2
        update(s,mid,n*2,ts,te,v)
        update(mid+1,e,n*2+1,ts,te,v)
        seg[n]=seg[n*2]+seg[n*2+1]

def find(s,e,n,ts,te):
    prop(s,e,n)
    if ts>e or te<s:
        return 0
    elif ts<=s<=e<=te:
        return seg[n]
    else:
        mid = (s + e) // 2
        return find(s,mid,n*2,ts,te)+find(mid+1,e,n*2+1,ts,te)

for _ in range(m):
    q,*v = map(int,input().split())
    if q==1:
        update(1,start,1,v[0],v[1],v[2])
    else:
        sys.stdout.write(str(find(1,start,1,v[0],v[0]))+'\n')

