import sys
st="x"
while st !="":
    st = input().split("$")[0].replace(" ","")

    stack = [[]]
    open=False
    for char in st:
        if char=="(":
            stack.append([])
            open=True
        elif char == ")":
            rep=""
            while len(stack[-1]) >0 and stack[-1][-1].isnumeric():
                rep+=stack[-1].pop()
            stack[-1]=stack[-1]*int(rep[::-1])
            temp=stack.pop()
            stack[-1].extend(temp)
        else:
            stack[-1].append(char)
    for i in stack[0]:
        sys.stdout.write(i)
    sys.stdout.write("\n")
