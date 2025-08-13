from collections import deque

def solution(plans):
    answer = []
    seq = []
    schedule = []
    for _ in plans:
        sub,start,time = _
        mins = list(start.split(":"))
        toMin = int(mins[0])*60+int(mins[1])
        time = int(time)
        seq.append((toMin, time, sub))
    seq.sort()
    seq = deque(seq)
    time = seq[0][0]
    left = []
    while seq:
        cur=seq.popleft()
        if seq:
            nextTime = seq[0][0]
        else:
            nextTime = 10**10
        if nextTime>=cur[1]+time:
            answer.append(cur[2])
            time += cur[1]
            while left and time<nextTime:
                cur = left.pop()
                if nextTime>=cur[1]+time:
                    answer.append(cur[2])
                    time += cur[1]
                else:
                    left.append((cur[0],cur[1]-(nextTime-time),cur[2]))
                    time = nextTime
        else:
            left.append((cur[0],cur[1]-(nextTime-time),cur[2]))
        time = nextTime
                    
    return answer