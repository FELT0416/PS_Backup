from collections import deque

n,k = map(int,input().split())
seq = list(map(int,input().split()))

def sorts(li, ind):
    temp = []
    flip = li[ind:ind+k]
    flip.reverse()
    for _ in range(n):
        if _ <ind or _>ind+k-1:
            temp.append(li[_])
        if _==ind:
            temp.extend(flip)
    return temp

def hash(li):
    ret = 0
    for ind, val in enumerate(li):
        ret+=val*(10**ind)
    return ret
pos = [i for i in range(n-k+1)]

start = deque([(seq,0)])
target = sorted(seq)
visited = {hash(seq)}
ans = -1

while start:
    cur, cnt = start.popleft()
    if cur == target:
        ans = cnt
        break
    for _ in pos:
        temp = sorts(cur, _)
        ch = hash(temp)
        if ch not in visited:
            start.append((temp,cnt+1))
            visited.add(ch)

print(ans)
