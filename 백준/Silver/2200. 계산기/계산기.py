n = int(input())
seq = list(map(int, input().split()))

ans = 0
for ind, val in enumerate(seq):
    if ind == 0:
        ans+=1
        continue
    else:
        if val != 0:
            ans+=1 #덧셈
            while val != 0:
                val//=10
                ans+=1
        if ind != len(seq)-1:
            ans+=2
        else:
            ans+=1
print(ans)
