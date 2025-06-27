def solution(record):
    
    usernames = {}
    logs = []
    for rec in record:
        log = rec.split()
        if log[0]=="Enter":
            usernames[log[1]]=log[2]
            logs.append((log[1],1))
        elif log[0]=="Leave":
            logs.append((log[1],0))
        elif log[0]=="Change":
            usernames[log[1]] = log[2]
    answer = []
    for ans in logs:
        if ans[1]==1:
            answer.append(f'{usernames[ans[0]]}님이 들어왔습니다.')
        elif ans[1]==0:
            answer.append(f'{usernames[ans[0]]}님이 나갔습니다.')
    
    
    
    return answer