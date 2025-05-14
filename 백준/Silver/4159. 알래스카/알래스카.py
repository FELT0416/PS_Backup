while True:
    n = int(input())
    if n == 0:
        break
    charge=[]
    for _ in range(n):
        charge.append(int(input()))

    charge.sort()
    prev = 0
    ch = True
    for i in charge:
        if i - prev > 200:
            break
        prev = i

    if 1422 - prev > 100:
        ch = False

    if ch:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
