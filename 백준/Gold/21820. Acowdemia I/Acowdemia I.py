n, a = map(int, input().split())
papers = list(map(int,input().split()))

papers.sort(reverse=True)
cite={papers[0]:1}
count = {papers[0]:1}
toCheck =[]
for i in range(1,n):
    if papers[i] in cite:
        cite[papers[i]]+=1
        count[papers[i]]+=1
    else:
        cite[papers[i]]=cite[papers[i-1]]+1
        count[papers[i]] = 1
h = 0
for i in cite:
    if cite[i]>=i:
        if h < i:
            h = i
    else:
        if h < cite[i]:
            h=cite[i]
    check = min(count[i], a)
    if i+1 in count:
        citeI = cite[i+1]
    else:
        citeI = cite[i]-count[i]
    if check + citeI >= i+1:
        if h < i+1:
            h=i+1
print(h)