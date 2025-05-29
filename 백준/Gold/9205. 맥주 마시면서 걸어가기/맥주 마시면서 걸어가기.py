from collections import deque
rep = int(input())
for _ in range(rep):
    n = int(input())
    start = tuple(map(int, input().split()))
    checkpoint = [tuple(map(int, input().split())) for _ in range(n)]
    target = tuple(map(int, input().split()))

    queue = deque([start])
    visited = set()
    ans = False

    while queue:
        x,y = queue.pop()
        if abs(x-target[0])+abs(y-target[1]) <= 1000:
            ans = True
            break

        for cx, cy in checkpoint:
            if abs(x-cx)+abs(y-cy)<=1000 and (cx,cy) not in visited:
                queue.append((cx,cy))
                visited.add((cx,cy))
    if ans:
        print("happy")
    else:
        print("sad")

