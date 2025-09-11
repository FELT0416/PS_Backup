import sys, heapq
reps = int(input())
for _ in range(reps):
    mo, n = map(int, input().split())
    prod = []
    for _ in range(n):
        types, *p, b = map(int, input().split())
        p.sort()
        prod.append([p,b])
        mo-=p[0]*b
    if mo<0:
        print("IMPOSSIBLE")
    else:
        dp = []
        for p, b in prod:
            temp =[]
            for i in range(1,len(p)):
                if p[i]*b-p[i-1]*b !=0:
                    temp.append(p[i]*b-p[0]*b)
            dp.append(temp)
        sets ={0}
        ans = 0
        for i in dp:
            check = sets.copy()
            for ch in check:
                for j in i:
                    if ch+j <= mo:
                        sets.add(ch+j)
                        if ch+j >ans:
                            ans=ch+j
                    else:
                        break
        print(mo-ans)