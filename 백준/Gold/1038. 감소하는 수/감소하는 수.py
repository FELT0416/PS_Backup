def generate():
    ans = [0]


    def backtrack(digit, num=0):
        if len(str(num)) == digit and num !=0:
            ans.append(num)
            return
        if len(str(num)) > digit:
            return

        if num ==0:
            for i in range(1,10):
                num = i
                backtrack(digit, num)
        else:
            for i in range(10):
                if num%10<=i:
                    continue
                num *= 10
                num+=i
                backtrack(digit, num)
                num //= 10




    for i in range(1,11):
        backtrack(i)
    return ans

seq = generate()

n = int(input())

try:
    print(seq[n])
except IndexError:
    print("-1")