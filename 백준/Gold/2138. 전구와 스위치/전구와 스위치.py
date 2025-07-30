n = int(input())
cur = [int(a) for a in input()]
target = [int(a) for a in input()]

def switch(ind):
    def toggle(i):
        if cur[i]==0:
            cur[i]=1
        else:
            cur[i]=0
    toggle(ind)
    if ind >0:
        toggle(ind-1)
    if ind+1<len(cur):
        toggle(ind+1)
    return

temp = cur.copy()

cnt = 0
ans = -1
for _ in range(1,n):
    if cur[_-1]!=target[_-1]:
        switch(_)
        cnt+=1
if cur == target:
    ans = cnt


cur = temp
switch(0)
cnt=1
for _ in range(1,n):
    if cur[_-1]!=target[_-1]:
        switch(_)
        cnt+=1
if cur == target:
    if ans == -1:
        ans = cnt
    else:
        ans = min(cnt,ans)
print(ans)