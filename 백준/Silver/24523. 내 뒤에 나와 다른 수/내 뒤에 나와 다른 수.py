import sys
n = int(input())
seq = list(map(int, input().split()))

cnt = 0
chk = seq[0]
for ind, val in enumerate(seq):
    if chk == val:
        cnt += 1
    else:
        for _ in range(cnt):
            sys.stdout.write(str(ind+1)+" ")
            chk = val
            cnt = 1
for _ in range(cnt):
    sys.stdout.write("-1"+" ")