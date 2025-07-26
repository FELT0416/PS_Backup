import sys
input=sys.stdin.readline

ans = []
def solve(num=[]):
    if len(num)==n+1:
        ans.append(num[:])
        return
    if len(num)==0:
        for _ in range(10):
            num.append(_)
            solve(num)
            num.pop()
    else:
        check = seq[len(num)-1]
        if check == ">":
            large=True
        else:
            large=False

        for _ in range(10):
            if _ in num:
                continue
            if large:
                if num[-1]>_:
                    num.append(_)
                    solve(num)
                    num.pop()
            else:
                if num[-1]<_:
                    num.append(_)
                    solve(num)
                    num.pop()



n = int(input())
seq = list(input().split())
solve()
ans.sort()
for _ in ans[-1]:
    sys.stdout.write(str(_))
sys.stdout.write("\n")
for _ in ans[0]:
    sys.stdout.write(str(_))