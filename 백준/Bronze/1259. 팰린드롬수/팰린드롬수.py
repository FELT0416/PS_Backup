import sys

def checkPen(st):
    mid = (len(st)-1)//2

    for i in range(mid+1):
        #print(st[i], st[-i-1])
        if st[i]!=st[-i-1]:
            sys.stdout.write("no\n")
            return
    sys.stdout.write("yes\n")
    return

while True:
    temp = sys.stdin.readline().strip()
    if temp == "0":
        break
    checkPen(temp)