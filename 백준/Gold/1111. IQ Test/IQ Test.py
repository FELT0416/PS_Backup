n = int(input())
seq = list(map(int,input().split()))


def solve(a,b):
    for _ in range(1,n):
        if seq[_]==seq[_-1]*a+b:
            continue
        else:
            return False
    return True


if n == 1:
    print('A')
else:
    ans = set()
    for _ in range(-500, 500):
        a = _
        b = seq[1]-seq[0]*a
        if solve(a,b):
            ans.add(seq[-1]*a+b)

    if len(ans)==0:
        print("B")
    elif len(ans)==1:
        print(list(ans)[0])
    else:
        print("A")