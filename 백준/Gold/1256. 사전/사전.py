import math
def solve(a,z,k):
    ans = ""
    while a!=0 and z!=0:
        abound = math.comb(z + a - 1, z)  # a를 제일 앞에 뒀을 때 경우의 수
        zbound = math.comb(z + a - 1, z - 1)  # z를 제일 앞에 뒀을 때 경우의 수
        if 0<k<=abound:
            ans+="a"
            a -=1
        elif abound<k<=abound+zbound:
            ans+="z"
            k-=abound
            z-=1
        else:
            return -1
    ans+="a"*a
    ans+="z"*z
    return ans
n, m, k = map(int,input().split())
print(solve(n,m,k))