import sys
input=sys.stdin.readline

n,m = map(int,input().split())
alice = [list(input())for i in range(n)]
bob = [list(input()) for i in range(n)]

turnA = []
turnB = []
for i in alice:
    temp = 0
    for c in i:
        if c == "B":
            temp+=1
    turnA.append(temp)
for i in bob:
    temp = 0
    for c in i:
        if c == "A":
            temp+=1
    turnB.append(temp)


ta = sum(turnA)
tb = sum(turnB)
if turnA[-1] != 0:
    ta-=1
if turnB[-1] != 0:
    tb-=1
if ta <=tb:
    print("Alice")
else:
    print("Bob")

rep = int(input())
for _ in range(rep):
    y1,x1,y2,x2 = map(int,input().split())
    if alice[y1-1][x1-1] != bob[y2-1][x2-1]:
        if alice[y1-1][x1-1] == "A":
            alice[y1 - 1][x1 - 1] = "B"
            bob[y2 - 1][x2 - 1] = "A"
            turnA[y1-1]+=1
            turnB[y2-1]+=1
        else:
            alice[y1 - 1][x1 - 1] = "A"
            bob[y2 - 1][x2 - 1] = "B"
            turnA[y1 - 1] -= 1
            turnB[y2 - 1] -= 1
    ta = sum(turnA)
    tb = sum(turnB)
    if turnA[-1] != 0:
        ta -= 1
    if turnB[-1] != 0:
        tb -= 1
    if ta <= tb:
        print("Alice")
    else:
        print("Bob")