import sys
input=sys.stdin.readline
sys.setrecursionlimit(10*1000)

def build(n):
    length = 1
    while length<n:
        length*=2
    seg = [0]*(length*2)
    for _ in range(1,n+1):
        seg[length+_-1]= 1
    for ind in range(length-1,0,-1):
        seg[ind]= seg[ind*2]+seg[ind*2+1]
    return seg

n,k = map(int,input().split())
seg = build(n)

def pop(seg,n):
    length = len(seg)//2 # 원래 배열 시작 인덱스 번호
    def find(node,target):
        if node>=length:
            return node-length+1
        left = seg[node*2]
        right = seg[node*2+1]
        if target <=left:
            return find(node*2,target)
        elif target<=right+left:
            return find(node*2+1,target-left)
    def update(node):
        cur = length+node-1
        while cur >=1:
            seg[cur] -= 1
            cur//=2
    check = find(1,n)
    update(check)
    return seg, check

ans = []
node = k
inc = k-1
while len(ans)!=n:
    seg, a = pop(seg,k)
    ans.append(a)
    k+=inc
    if k>seg[1]:
        if seg[1]==0:
            break
        k%=seg[1]
        if k==0:
            k=seg[1]
s = "<" + ", ".join(map(str, ans)) + ">"
sys.stdout.write(s)