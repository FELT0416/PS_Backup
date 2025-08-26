import sys
input = sys.stdin.readline

n,k,d = map(int,input().split())

algo = {}
skill = []
for _ in range(n):
    j,k = map(int,input().split())
    al = set(map(int,input().split()))
    skill.append((k,_))
    algo[_]=al

skill.sort()
p1 = 0
p2 = 0


group = {}
ans = 0
while p2<n:
    while p2<n and skill[p2][0]-skill[p1][0]<=d:
        user = skill[p2][1]
        members = p2-p1+1
        union = 0
        for al in algo[user]:
            if al in group:
                group[al]+=1
            else:
                group[al]=1
            if group[al]==members:
                union +=1
        temp = (len(group.keys())-union)*members
        ans = max(ans,temp)
        p2+=1
    if p2==n:
        break
    curMinSkill = skill[p1][0]
    while p1<n and skill[p1][0]==curMinSkill:
        user = skill[p1][1]
        for al in algo[user]:
            if al in group:
                group[al]-=1
                if group[al]==0:
                    del group[al]
        p1+=1

print(ans)
