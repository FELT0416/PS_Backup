import sys
input = sys.stdin.readline
n=int(input())
tree = {}
start = set()
for _ in range(n):
    k, *seq = input().split()
    path = "s"
    for ind, val in enumerate(seq):
        if ind > 0:
            prev = seq[ind-1]
            if (prev,ind-1,path) not in tree:
                tree[(prev,ind-1,path)]={(val,ind,path+prev)}
            else:
                tree[(prev,ind-1,path)].add((val,ind,path+prev))
            path += prev
        else:
            start.add((val,ind,'s'))

toVisit = sorted(list(start),reverse=True)
prefix="--"
while toVisit:
    cur = toVisit.pop()
    sys.stdout.write(prefix*cur[1]+cur[0]+"\n")
    if cur in tree:
        temp = sorted(list(tree[cur]),reverse=True)
        toVisit.extend(temp)