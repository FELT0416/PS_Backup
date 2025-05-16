"""
브루트포스 > 2730000 가지 경우의 수 
교집합 연산 = O(10)
최대 10개 >
273000000 > 가능할지도?
"""

def solution(n, q, ans):
    answer = 0
    possible=[]
    for x1 in range(1,27):
        for x2 in range(x1+1,n-2):
            for x3 in range(x2+1,n-1):
                for x4 in range(x3+1,n):
                    for x5 in range(x4+1,n+1):
                        possible.append({x1,x2,x3,x4,x5})
    for i in possible:
        check = True
        for ind in range(len(ans)):
            if len(i&set(q[ind])) != ans[ind]:
                check=False
                break
        if check:
            answer+=1

    return answer