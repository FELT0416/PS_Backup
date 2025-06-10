start = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
ans = [10,55]

for _ in range(10):
    sums = sum(start[-1])
    temp = []
    for i in start[-1]:
        temp.append(sums%1000000007)
        sums-=i
    start.append(temp)
    ans.append((ans[-1]+sum(temp))%1000000007)
n = int(input())
for i in range(n):
    x = int(input())
    if len(start)<x:
        while len(start)<=x:
            sums = sum(start[-1])
            temp = []
            for i in start[-1]:
                temp.append(sums % 1000000007)
                sums -= i
            start.append(temp)
            ans.append((ans[-1] + sum(temp)) % 1000000007)
    print(ans[x-1])