import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
ppl = list(map(int,input().split()))
tree = [[]for _ in range(n)]
for _ in range(n-1):
    a,b= map(int,input().split())
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)

dp =[[-1,-1,-1]for _ in range(n)] #n이 우수마을일때, 아니지만 자식에 우수마을이 있을 때, 자식과 n 모두 우수마을이 아닐 때(부모 강제)
visited={0}
def dfs(node,parent=-1):
    #리프 노드 조건분기
    if len(tree[node])==1 and parent !=-1:
        dp[node][0]=ppl[node] # 우수 마을
        dp[node][1]=0 # 우수 마을 x
        dp[node][2]=0
        return

    for child in tree[node]:
        if child == parent:
            continue
        dfs(child, node) # 자식 노드 dp 테이블 채우기
    good = 0 #dp0, 무조건 자식들은 모두 우수 x (max dp1,dp2) + tree[node]
    bad = 0 #dp1 무조건 자식 중 하나는 우수 # (max dp1, dp2,dp3) 후, 모든 선택값에 dp1이 없으면, loss 가 가장 적은 마을을 우수마을로 지정
    bad2 = 0 #dp2 무조건 자식은 모두 우수 x (max dp1,dp2)
    loss = float("inf")
    for child in tree[node]:
        if child == parent:
            continue
        temp = max(dp[child][1],dp[child][2])
        good += temp
        bad += max(dp[child][0],temp)
        bad2 += dp[child][1]
        loss = min(temp - dp[child][0], loss)
    dp[node][0]=good+ppl[node]
    dp[node][2]=bad2
    dp[node][1]=min(bad,bad-loss)
    return

dfs(0)
print(max(dp[0][0],dp[0][1],dp[0][2]))