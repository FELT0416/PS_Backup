n = int(input())
cute = 0
notcute = 0
for _ in range(n):
    chk = int(input())
    if chk ==0:
        notcute+=1
    else:
        cute+=1
if notcute<cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")