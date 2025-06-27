def solution(bandage, health, attacks):
    answer = 0
    
    curH=health
    prev=0
    for time, damage in attacks:
        curH+=((time-prev-1)//bandage[0])*bandage[2]+(time-prev-1)*bandage[1]
        if curH>health:
            curH=health
        curH-=damage
        
        if curH<=0:
            answer=-1
            break
        else:
            answer= curH
        prev = time
    
    return answer