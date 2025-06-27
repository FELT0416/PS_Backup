def solution(board):
    answer = 1
    diag = [[board[0][0],board[1][1],board[2][2]],[board[2][0],board[1][1],board[0][2]]]
    vert = [[board[0][0],board[1][0],board[2][0]],
            [board[0][1],board[1][1],board[2][1]],
            [board[0][2],board[1][2],board[2][2]]
           ]
    hor = [list(i) for i in board]
    bingo = 0
    status = ""
    dup = set()
    
    for _ in diag:
        if _ == ['O','O','O']:
            bingo+=1
            status+='o'
        elif _ == ['X','X','X']:
            status+='x'
            bingo+=1
    for _ in vert:
        if _ == ['O','O','O']:
            bingo+=1
            status+='o'
        elif _ == ['X','X','X']:
            status+='x'
            bingo+=1
    for _ in hor:
        if _ == ['O','O','O']:
            bingo+=1
            status+='o'
        elif _ == ['X','X','X']:
            status+='x'
            bingo+=1

    x=0
    o=0
    for _ in board:
        for i in _:
            if i =='X':
                x+=1
            elif i=='O':
                o+=1
    if status=="o"or status=="x" or status=="oo" or status=="xx":
        if status=="x"or status=="xx":
            if o!=x:
                answer=0
        else:
            if o-1!=x:
                answer=0
    elif status =="":
        if o-1!=x and o!=x:
            answer=0
    else:
        answer=0
        
    print(status,o,x)
    
    
    return answer