n = int(input())
lista = list(map(int,input().split()))
listb = list(map(int,input().split()))

original = {}
now = {}


for ind in range(n):
    original[lista[ind]] = ind
    now[listb[ind]] = ind
ans = []
amount = 0
for key in now:
    increase = now[key]-original[key]
    if increase == amount:
        ans.append(key)
    elif amount > increase:
        amount = min(amount, increase)
        ans = [key]
print(*ans)