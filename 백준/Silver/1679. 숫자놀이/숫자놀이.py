import sys
input=sys.stdin.readline


n = int(input())
ints = list(map(int,input().split()))
k = int(input())

ints.sort()
dp = {0:0}

for _ in range(k):
    keys = dp.copy()
    for key in keys:
        for prev in ints:
            check = key+prev
            if check not in keys:
                dp[check]=dp[key]+1

for _ in range(ints[-1]*k+2):
    if _ not in dp:
        if _%2==0:
            print(f'holsoon win at {_}')
        else:
            print(f'jjaksoon win at {_}')
        break