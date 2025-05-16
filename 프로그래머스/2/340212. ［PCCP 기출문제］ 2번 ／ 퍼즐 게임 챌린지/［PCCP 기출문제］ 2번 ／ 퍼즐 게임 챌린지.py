"""
0, max(diffs) 범위로 이분탐색
"""

def solution(diffs, times, limit):
    def solve(diffs, times, lvl):
        diffs.append(0)
        times.append(0)
        time = 0
        p = 0
        while p<len(diffs):
            if diffs[p]<=lvl:
                time+=times[p]
                p+=1
            else:
                time+=(diffs[p]-lvl)*(times[p]+times[p-1])+times[p]
                p+=1
            if time > limit:
                return False
        return True
    
    left = 1
    right = 100000
    while left!=right:
        print(left,right)
        lvl = (left+right)//2
        check = solve(diffs, times, lvl)
        if check:
            right = lvl
        else:
            left = lvl+1
    
    answer = left
    return answer