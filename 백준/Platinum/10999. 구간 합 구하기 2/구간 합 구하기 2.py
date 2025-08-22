import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*8)


n,m,k = map(int,input().split())
li = [int(input()) for _ in range(n)]

start = 1
while start <=n:
    start<<=1
length = start*2
seg = [0]*length
lazy = [0]*length
for ind, val in enumerate(li):
    seg[start+ind]=val
for ind in range(start-1,0,-1):
    seg[ind]=seg[ind*2]+seg[ind*2+1]

def find(s,e,n,ts,te):
    prop(s,e,n)
    if te<s or e<ts:
        return 0
    elif ts<=s<=e<=te:
        return seg[n]
    else:
        mid = (s+e)//2
        return find(s,mid,n*2,ts,te)+find(mid+1,e,n*2+1,ts,te)

def update(s,e,n,v,ts,te):
    prop(s, e, n)
    if te<s or e<ts:
        return
    elif ts<=s<=e<=te:
        lazy[n]+=v
        prop(s, e, n)
    else:
        mid = (s + e) // 2
        update(s,mid,n*2,v,ts,te)
        update(mid+1,e,n*2+1,v,ts,te)
        seg[n]=seg[n*2]+seg[n*2+1]

def prop(s,e,n):
    if n<length//2:
        lazy[n*2]+=lazy[n]
        lazy[n*2+1]+=lazy[n]
    seg[n]+=lazy[n]*(e-s+1)
    lazy[n]=0
    return


for _ in range(m+k):
    q,*v = map(int,input().split())
    if q==1:
        update(1,start,1,v[2],v[0],v[1])
    elif q==2:
        ans = find(1,start,1,v[0],v[1])
        sys.stdout.write(str(ans)+'\n')