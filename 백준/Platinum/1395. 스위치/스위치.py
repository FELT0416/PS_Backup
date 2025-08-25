import sys
input=sys.stdin.readline

n,m = map(int,input().split())

start = 1
while start<n:
    start<<=1
length = start*2
seg = [0]*length
lazy = [0]*length


def prop(s,e,n):
    if n<start:
        lazy[n*2]+=lazy[n]
        lazy[n*2+1]+=lazy[n]
    if lazy[n]%2!=0:
        seg[n]=(e-s+1 - seg[n])
    lazy[n]=0


def find(s,e,n,ts,te):
    prop(s,e,n)
    if te<s or e<ts:
        return 0
    elif ts<=s<=e<=te:
        return seg[n]
    else:
        mid = (s+e)//2
        return find(s,mid,n*2,ts,te)+find(mid+1,e,n*2+1,ts,te)

def update(s,e,n,ts,te):
    prop(s,e,n)
    if te<s or e<ts:
        return
    elif ts<=s<=e<=te:
        lazy[n]+=1
        prop(s,e,n)
    else:
        mid = (s + e) // 2
        update(s, mid, n * 2, ts, te)
        update(mid + 1, e, n * 2 + 1, ts, te)
        seg[n]=seg[n*2]+seg[n*2+1]

for _ in range(m):
    q,a,b = map(int,input().split())
    if q == 0:
        update(1,start,1,a,b)
    else:
        sys.stdout.write(str(find(1,start,1,a,b))+"\n")

