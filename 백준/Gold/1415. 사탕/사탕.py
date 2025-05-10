n = int(input())
candy = []
for i in range(n):
    candy.append(int(input()))
candy.sort()

prime = list(range(2, candy[-1] * n + 1))
for i in range(len(prime)):
    if prime[i] == -1:
        continue
    current_prime = prime[i]
    if current_prime ** 2 > candy[-1] * n:
        break
    for j in range(i + current_prime, len(prime), current_prime):
        prime[j] = -1

primeSet = set(prime)

combs={0:1}

def getComb():
    for i in range(n):
        if i>0 and candy[i-1]==candy[i]:
            continue
        count=1
        while i+count <= len(candy)-1 and candy[i]==candy[i+count]:
            count+=1
        keys = combs.copy()
        for key in keys:
            for j in range(1, count+1):
                if key + candy[i]*j in combs:
                    combs[key + candy[i]*j] += keys[key]
                else:
                    combs[key + candy[i]*j] = keys[key]
    ans = 0
    for i in combs.keys():
        if i in primeSet:
            ans += combs[i]
    return ans

print(getComb())