def nQueen(n, count=0, x1 = set(),diag1 = set(), diag2 = set()):
    if count == n: # n개의 퀸을 전부 배치 완료했을 때 1 리턴
        return 1

    ans=0

    #x1 = x행 체크
    #diag1 =  x-y 인 대각선 체크
    #diag2 =  0행 기준 대각선의 위치 (0,n에서 시작하는 대각선이면 1,n-1...으로 향하는 대각선)
    #y열은 일일히 체크할 것이기때문에 필요X

    for x in range(n): #모든 x 탐색
        if x not in x1 and x-count not in diag1 and x+count not in diag2: # 퀸이 배치가능할 경우
            x1.add(x)
            diag1.add(x-count)
            diag2.add(x+count)
            ans+=nQueen(n,count+1, x1,diag1,diag2)
            x1.remove(x)
            diag1.remove(x-count)
            diag2.remove(x+count)

    return ans

n=int(input())

print(nQueen(n))