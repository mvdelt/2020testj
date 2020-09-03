def solution(tickets):
    seq=[["", "ICN"]]
    for i in range(len(tickets)):    
        last_st = seq[-1][1]
        t_list = sorted([t for t in tickets if t[0]==last_st], key=lambda x: x[1])
        if len(t_list)>0: seq.append(t_list[0]); continue
            
        popped = seq.pop(-1)
        
        last_st = seq[-1][1]
        t_list = sorted([t for t in tickets if t[0]==last_st], key=lambda x: x[1])
        popped_idx = t_list.index(popped)
        t_list = t_list[popped_idx+1:]
        
        

        
        if i==0:
            t_list = sorted([t for t in tickets if t[0]=="ICN"], key=lambda x: x[1])
            seq.append(t_list[0])
            continue
        
        
    
    
    
    answer = []
    return answer