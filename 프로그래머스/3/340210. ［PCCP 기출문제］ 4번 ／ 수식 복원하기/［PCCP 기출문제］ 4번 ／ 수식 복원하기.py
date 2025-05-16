"""
각각의 자릿수를 비교

A - B = C
해당 수식의 진법은
A-B < 0 이면, 
C - A + B or C-A+B-1 (아랫 자리에서 발생했을수도)

A + B = C
min(A,B) > C 라면,

A+B-C or A+B-C+1 진수가 된다 
"""
def solution(expressions):
    
    def solve(exp,n):
        a,b = map(int, (exp[0],exp[2]))
        op = exp[1]
        if exp[4] == "X":
            op = None
            ans = 0
        else:
            ans = int(exp[4])
        prevA=0
        prevB=0
        while a!=0 and b!=0:
            da = a%10
            db = b%10
            dans = ans%10
            if op == '-':
                if da-db <0:
                    a-=10
                    n = {dans - da + db}
                    return n
            elif op == '+':
                if min(da,db)>dans:
                    n = {da+db-dans}
                    return n
            for i in n.copy():
                if i <= max(da,db,dans):
                    n.remove(i)
            a//=10
            b//=10
            ans//=10
        return n
    
    def fill(exp,n):
        a,b = map(int, (exp[0],exp[2]))
        op = exp[1]
        poss = set()
        for i in n:
            if len(poss)>1:
                break
            temp1 = a
            temp2 = b
            na = 0
            ch = 1
            while temp1 !=0:
                na += (temp1%10) * ch
                ch*=i
                temp1//=10
            nb=0
            ch=1
            while temp2 !=0:
                nb += (temp2%10) * ch
                ch*=i
                temp2//=10
            if op == "+":
                ans = na+nb
            else:
                ans = na-nb
            ret = ""
            print(na,nb,ans)
            if ans ==0:
                ret+="0"
            while ans !=0:
                ret+=str(ans%i)
                ans//=i
            poss.add(ret[::-1])
        if len(poss)==1:
            return(list(poss)[0])
        else:
            return("?")
        
    
    n = {i for i in range(2,10)} # n진법
    simple = [i.split() for i in expressions]
    toCheck = [] # 지워진 수식의 인덱스
    for i in range(len(simple)):
        if simple[i][-1]=="X":
            toCheck.append(i)
        if len(n)!=1:
            n = solve(simple[i],n)
    answer = []
    for i in toCheck:
        exp = simple[i]
        exp[4] = fill(exp,n)
        temp = exp[0]
        for i in range(1,len(exp)):
            temp+=" "+exp[i]
        answer.append(temp)
        
    
    return answer