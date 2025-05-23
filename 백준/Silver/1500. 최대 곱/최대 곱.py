s, k = map(int, input().split())
d = s//k 
r = s%k  
result = d**(k-r)*(d+1)**r
print(result)