import sys
#입력
text = input()
toFind = input()

#전처리 과정
skip = [0]*len(toFind)
count=0

i=1
count=0
while i<len(toFind):
    if toFind[i]==toFind[count]:
        count += 1
        skip[i] = count
        i += 1
        continue
    if count!=0:
        count = skip[count-1]
    elif count ==0:
        i+=1

#찾기
ans=[] # 일치하는 좌표를 담는 리스트

curInd=0
checkInd = 0
while checkInd < len(text):
    if curInd == len(toFind)-1 and toFind[curInd]==text[checkInd]: # 문자열을 찾은 경우
        ans.append(checkInd-curInd+1)
        curInd = skip[curInd]
        checkInd+=1
        continue
    if toFind[curInd]==text[checkInd]:
        curInd+=1
        checkInd+=1
        continue
    else:
        if curInd==0:
            checkInd+=1
        else:
            curInd = skip[curInd-1]
        continue

print(len(ans))
for i in ans:
    sys.stdout.write(str(i)+'\n')