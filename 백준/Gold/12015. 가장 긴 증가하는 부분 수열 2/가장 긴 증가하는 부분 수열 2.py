#고민 끝에 풀이 찾아봄
import bisect
n = int(input())
seq = list(map(int,input().split()))
lis = [seq[0]]

for i in range(1,n):
    check = seq[i]
    addind = bisect.bisect_left(lis,check)
    if addind == len(lis):
        lis.append(check)
    else:
        lis[addind]=check

print(len(lis))
