d,n = map(int,input().split())
oven = list(map(int,input().split()))
pizza = list(map(int,input().split()))


prev = 1000000000
for ind, val in enumerate(oven):
    oven[ind]=min(prev,val)
    prev = oven[ind]

ans = True
for ind,size in enumerate(pizza):
    if not oven:
        ans = False
        break
    while oven and size>oven[-1]:
        oven.pop()
    if not oven:
        ans = False
        break
    if oven:
        oven.pop()
if ans:
    print(len(oven)+1)
else:
    print(0)