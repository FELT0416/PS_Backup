for _ in range(3):
    n = int(input())
    sums = 0
    for i in range(n):
        sums += int(input())
    if sums>0:
        print("+")
    elif sums==0:
        print(0)
    else:
        print("-")