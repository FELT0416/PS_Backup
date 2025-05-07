import bisect

n = int(input())
seq = list(map(int, input().split()))

lis = [seq[0]]
maps = [[(seq[0],-1)]] # 각 원소의 직전 원소를 가르키는 리스트

for i in range(1, n):
    ind = bisect.bisect_left(lis,seq[i])
    if ind == len(lis):
        lis.append(seq[i])
        maps.append([(seq[i],len(maps[-1]))])
    else:
        lis[ind]=seq[i]
        if ind == 0:
            length=-1
        else:
            length= len(maps[ind-1])
        maps[ind].append((seq[i],length))

ans=[]
toGo = 1 # 가장 첫번째 lis
for i in range(len(lis)-1,-1,-1):
    ans.append(maps[i][toGo-1][0])
    toGo = maps[i][toGo-1][1]

ans.reverse()
print(len(ans))
print(*ans)
