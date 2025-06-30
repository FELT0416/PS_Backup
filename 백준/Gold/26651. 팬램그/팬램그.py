n = int(input())
if n ==0:
    print("A")
else:
    ans =[]
    while n>3:
        a = int(n**0.5)
        ans.append(a)
        n-=a**2
    default = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = ""
    for _ in ans:
        string+="A"*(_-1)
        string+=default
        string+="Z"*(_-1)
    if n>0:
        for _ in range(n-1):
            string+="A"
        string+=default
    print(string)
