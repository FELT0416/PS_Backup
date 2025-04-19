"""
작은 직사각형이 오면 > 더 큰 직사각형은 전부 스택에서 제거 > 넓이 계산
"""
while True:
    n, *heights = map(int, input().split())
    if n == 0:
        break

    stack = []
    ans = 0
    for i in heights:
        count = 1
        if stack and stack[-1][0] > i:
            while len(stack)!=0 and stack[-1][0] > i:
                area = stack[-1][0]*(count+stack[-1][1]-1) # 높이가 temp 인 직사각형의 넓이
                if area > ans:
                    ans = area
                count += stack[-1][1]
                stack.pop()
        elif stack and stack[-1][0] == i:
            stack[-1][1] += 1
            continue
        stack.append([i, count])
    #마지막에 스택에 남은것 처리
    count = 1
    while stack:
        area = stack[-1][0] * (count + stack[-1][1] - 1)  # 높이가 temp 인 직사각형의 넓이
        if area > ans:
            ans = area
        count += stack[-1][1]
        stack.pop()
    print(ans)



