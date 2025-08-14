import sys
input = sys.stdin.readline

n = input().strip()
temp = 10
ans =0
while int(n)>9:
    temp = 0
    ans+=1
    for val in n:
        val = int(val)
        temp+=val
    n = str(temp)
print(ans)
if int(n)%3==0:
    print("YES")
else:
    print("NO")