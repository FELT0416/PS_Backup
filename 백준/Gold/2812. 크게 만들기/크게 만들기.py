import sys
input=sys.stdin.readline
n, k=map(int, input().split())
num = input()

count = 0
ans = [num[0]]
ind = 1

while ind<n:
    check = num[ind]
    while len(ans)>0 and check>ans[-1] and count<k:
        ans.pop()
        count+=1
    ans.append(check)
    ind+=1

for i in range(n-k):
    sys.stdout.write(ans[i])