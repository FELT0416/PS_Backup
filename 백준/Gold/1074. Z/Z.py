N, r, c = map(int, input().split(" "))
r += 1
c += 1

check = True
while check:
    if r <= 2**(N-1) and c <= 2**(N-1):
        N -= 1
    else:
        check = False


ans = 0  
while N !=0:        
    if r > 2**(N-1):
        hor = 1
        r -= 2**(N-1)
    else:
        hor = 0
    
    if c > 2**(N-1):
        ver = 1
        c -= 2**(N-1)
    else:
        ver = 0
  
    
    ans += (2*hor+ver)*(2**(N-1)*2**(N-1))
    N -= 1
print(ans)
