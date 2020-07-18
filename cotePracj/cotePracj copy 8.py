def solution(gens, pls):
    
    gp_dict = {}    
    # i. 장르별 플레이수 합산, 장르별 정렬.
    # ex) gp_dict = {'classic':[sum_plays, (0,500), (1,200)], ...}
    for i, (g, p) in enumerate(zip(gens, pls)):        
        gp_dict.setdefault(g, [0]).append((i,p))
        gp_dict[g][0] += p        
    g_ordered_list = sorted(list(gp_dict.items()), key=lambda x: x[1][0], reverse=True)

    # i. 장르 내에서 곡별 정렬.
    answer = []
    for g in g_ordered_list:
        tup_list = g[1][1:]
        tup_list.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        if len(tup_list)>1:
            for tup in tup_list[:2]:
                answer.append(tup[0])
        else:
            answer.append(tup_list[0][0])
    
    return answer

gs = ["classic", "pop", "classic", "classic", "pop"]
ps = [500, 600, 150, 800, 2500]
print(solution(gs,ps))