import sys

rep, target = map(int, sys.stdin.readline().split())
items = []
for _ in range(rep):
    items.append(list(map(int,sys.stdin.readline().split())))

values=[0 for _ in range(target+1)]

for i in items:
    weight, val, count = i[0],i[1],i[2]
    temp=0
    counts =[]
    while count-2**temp > 0:
        count -=2**temp
        counts.append(2**temp)
        temp+=1
    counts.append(count)
    count=0
    for i in counts:
        for j in range(target, i-1,-1):
            if weight*i<=j:
                if values[j] < values[j-weight*i]+val*i:
                    values[j] = values[j-weight*i]+val*i
sys.stdout.write(str(values[target]))
sys.stdout.flush()