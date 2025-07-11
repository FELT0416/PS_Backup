from collections import Counter

n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))

ans = []
while a and b:
    temp = Counter(a) & Counter(b)
    if not temp:
        break
    target = max(temp.keys())
    ans.append(target)
    p1 = a.index(target)+1
    p2 = b.index(target)+1
    if p1<len(a):
        a=a[p1:]
    else:
        a=[]
    if p2<len(b):
        b=b[p2:]
    else:
        b=[]
print(len(ans))
print(*ans)