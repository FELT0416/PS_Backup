"""
초단위로 바꿔서 계산하기
"""

def solution(video_len, pos, op_start, op_end, commands):
    temp = video_len.split(":")
    vlen = int(temp[0])*60 + int(temp[1])
    temp = pos.split(":")
    p = int(temp[0])*60 + int(temp[1])
    temp = op_start.split(":")
    op = int(temp[0])*60 + int(temp[1])
    temp = op_end.split(":")
    ed = int(temp[0])*60 + int(temp[1])
    print(p, op, ed)
    def prev(p,op,ed):
        if op<=p<=ed:
            p=ed
        p-=10
        if op<=p<=ed:
            p=ed
        elif p < 0:
            p = 0 
        return p
    def nexts(p,op,ed):
        if op<=p<=ed:
            p=ed
        p += 10
        if op<=p<=ed:
            p=ed
        elif p > vlen:
            p = vlen
        return p
    for com in commands:
        print(com)
        if com=="next":
            p=nexts(p,op,ed)
        else:
            p=prev(p,op,ed)
        print(p)

    answer = ''
    if p<600:
        answer+='0'
    answer += str(p//60)+":"
    if p%60<10:
        answer+='0'
    answer+=str(p%60)
    return answer