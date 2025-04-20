import sys
n = int(sys.stdin.readline())
seq = []
for _ in range(n):
    seq.append(int(sys.stdin.readline()))
seq.sort()
for i in seq:
    sys.stdout.write(str(i)+"\n")