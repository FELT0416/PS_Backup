
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if a !=b:
    sorta = sorted(a)
    cnt = n-1
    ans =False
    while a!= sorta:
        changeind = a.index(sorta[cnt])
        a[changeind], a[cnt] = a[cnt], a[changeind]
        cnt-=1
        if b == a:
            ans = True
            break
    if ans:
        print(1)
    else:
        print(0)
else:
    print(1)