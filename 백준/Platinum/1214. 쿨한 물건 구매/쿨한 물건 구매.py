"""
q>p라고 가정하면,
q를 p로 나눈 나머지를 r이라고하면
q를 2번 사용했을때 나머지는 2r%p
...
즉 q*n 이하의 수에서는 p로 나누었을때 나머지가 0(p만 사용했을때)
p로 나누엇을때 나머지가 r (q를 한번 사용할때+r의 배수)
q로 나누었을때 나머지가 2r%p (q를 두번사용할때+r의 배수)
... n까지를 표현할 수 있다.
"""
d,p,q = map(int,input().split())

s = min(p,q)
l = max(p,q)
ans = float("inf")
check = 0
flag = True
while flag:
    if check > d:
        flag=False
    if flag:
        curans = (d-check+s-1)//s*s + check
    else:
        curans = check
    ans = min(ans,curans)
    check+=l
print(ans)
