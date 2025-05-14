import sys
input = sys.stdin.readline
rep = int(input())
for i in range(rep):
    n = int(input())
    temp = n
    bi = 0
    while temp > 1:
        temp//=2
        bi+=1
    tri = 0
    while n > 2:
        n//=3
        tri+=2
    if n ==2:
        tri+=1
    sys.stdout.write(str(bi)+" "+str(tri)+"\n")
