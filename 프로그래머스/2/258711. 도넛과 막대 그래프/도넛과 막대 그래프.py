#추가된 정점 구하는법 - 해당 노드로 돌아오는 간선이 없음
#이후 분리된 그래프를 bfs로 도넛, 막대, 8자 판별 > 
# 직선 판별 > bfs시 방문노드를 재방문X
# 도넛 마지막 탐색 노드는 첫 노드와 연결
# 한 노드에서 나가느 간선이 2개 > 8자
from collections import deque

def solution(edges):
    edges.sort()
    check = {i for i in range(1, edges[-1][0]+1)}
    nodes = {}
    for st, ed in edges:
        if st in nodes:
            nodes[st].append(ed)
        else:
            nodes[st]=[ed]
        if ed in check:
            check.remove(ed)
    for _ in check:
        if _ in nodes and len(nodes[_])>=2:
            target = _
    print(target)
    answer = [target,0,0,0]
    to_check = nodes[target]
    for checknode in to_check:
        queue = deque([checknode])
        visited = set()
        split = False
        con = False
        while queue:
            cur = queue.popleft()
            if cur in nodes:
                for _ in nodes[cur]:
                    if _ in visited:
                        con = True
                    else:
                        queue.append(_)
                        visited.add(_)
                if len(nodes[cur])>=2:
                    split = True
        if not split and not con:
            answer[2]+=1
        elif not split:
            answer[1]+=1
        else:
            answer[3]+=1
    

    
    
    return answer