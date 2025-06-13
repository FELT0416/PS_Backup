def gcm(a,b):
    tempa = min(a,b)
    tempb = max(a,b)
    while tempa !=0 and tempb!=0:
        tempb = tempb%tempa
        tempa,tempb = tempb,tempa
    return a*b/max(tempa,tempb)

n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    print(int(gcm(a,b)))