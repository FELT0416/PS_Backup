import sys
rep = int(input())
for _ in range(rep):
    n, size = map(int, sys.stdin.readline().split())
    seq = []
    for i in range((size+9)//10):
        temp = list(map(int,sys.stdin.readline().split()))
        seq.extend(temp)
    sseq = sorted(seq)
    dseq = {}
    for i in seq:
        if i in dseq:
            dseq[i]+=1
        else:
            dseq[i]=1
    p = 0
    ans=0
    for ch in seq:
        if sseq[p] == ch:
            p+=1
        else:
            dseq[ch]-=1
            ans+=1

    print(n,ans)