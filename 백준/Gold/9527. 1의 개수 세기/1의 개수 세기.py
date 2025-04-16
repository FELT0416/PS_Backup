def calc(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    check = 1
    ans=0
    temp = 0
    while check*2<=n:
        check*=2
        temp=check//2 + temp*2
        ans=temp
    n-=check
    ans+=n+1
    ans+=calc(n)
    return ans

a, b = map(int, input().split())
if a != 1:
    print(calc(b)-calc(a-1))
else:
    print(calc(b))