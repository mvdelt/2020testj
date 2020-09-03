# i. 2020.08.01.토욜저녁. 재귀호출로 깔끔히 해결!!!
# 근데 프로그래머스 테스트케이스 1번이 통과가 안되네;;; 머지;;; 일단자고내일보자;;;


# i. ---------------------설계 및 슈도코드.-----------------------------

# 0. DFS를 하되, 알파벳순서 우선으로.
# 0. findAndSort(t, tlist) 함수: tlist-t 중에서, [공항에서 사용할수있는 모든 티켓을 알파벳순정렬하여 리스트, 사용못하는티켓리스트] 반환.

# 1. findAndSort함수의 반환값인 리스트의 첫원소리스트의 각 원소에대해 findAndSort 적용.
#     첫원소리스트에 값이없으면, 
# 2. 리스트 원소갯수가 0이되면 완료한거.

# 0. sol 함수: 만약 리스트원소갯수가 1개면 앤서리스트에 append하고, 앤서리스트를 리턴.->아니다 이거아니다.
#             볼리스트 = 전체리스트-앤서리스트
#             현재리스트 돌면서,
#                 (볼리스트 - 지금 티켓 자신) (a공항에서 a공항으로 가는 티켓은 없다고 치면 이거 필요없음.)
#                 사용가능티켓잇으면 앤서리스트에 append 하고, 그 티켓에 대한 리스트를 인자로 재귀호출,            
#                 리턴값 0이면, 앤서리스트에서 remove하고, 다음원소.
#                 리턴값 0 아니면, 그값을 리턴.
#             다돌앗는데 없으면, 0리턴.
# -------------------------------------------------------------------------             



# def sol(sortedTickets):
#     for ticket in sortedTickets:
#         sortedTickets = findAndSort(ticket[1])
#     sol(sortedTickets)
    

def sol(tlist):    
    # if len(tlist)==1:
    #     ans_list.append(tlist[0])
    #     return ans_list    


    # 알파벳순으로 정렬.
    tlist = sorted(tlist, key=lambda x: x[1])

    # 최종조건.
    if len(ans_list)==len(allTickets)-1:
        ans_list.append(tlist[0])
        return ans_list

    
    # seelist = allTickets-ans_list 구현.
    seelist = allTickets[:]
    for x in ans_list:
        try:
            seelist.remove(x)
        except ValueError:
            pass

    for t in tlist:
        ntlist = [nt for nt in seelist if t[1]==nt[0]]
        if t in ntlist:
            ntlist.remove(t) # i. (a에서a로 가는 티켓도 만약 잇다면 요거 필요. a공항에서 a공항으로 가는 티켓은 없다고 치면 이거 필요없음.)
        if len(ntlist)!=0:
            ans_list.append(t)
            solret = sol(ntlist)
            if solret==0:
                ans_list.remove(t)
                continue
            else:
                return solret
    return 0
        

        
    # # 다음티켓들의 리스트
    # ntlist=[nt for nt in tlist if t[1]==nt[0]]
    # if len(ntlist)!=0: 
    #     ans_list.append(t)
    #     sol()
    # else:
            
    # # 리스트 돌면서,
    # for nt in ntlist:
        
    
    
    
ans_list=[]
allTickets=[]
def solution(ts):
    global allTickets
    allTickets=ts
    
    firstList=[t for t in ts if t[0]=="ICN"]
    solret = sol(firstList)

    assert len(solret)==len(ts), 'j) error! num not match!'
    print('solret:',solret)
    return ["ICN"]+ [i[1] for i in solret]



t_ex1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] # return should be: ["ICN", "JFK", "HND", "IAD"]
t_ex2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]] # return should be: ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
t_ex3 = [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
t_ex4 = [['ICN', 'COO'],['ICN', 'COO'], ['COO', 'ICN']]
t_ex5 = [['ICN', 'a'],['a', 'ICN'],['ICN', 'b'], ['b', 'c'], ['c', 'ICN'], ['ICN', 'd'],['d','e'],['e','ICN'],['ICN','f'],['f','g'],['g','h'],['h','i'],['i','g'],['g','a'],['a','ICN']]
t_ex6 = [['ICN','a'], ['a','b'],['b','a'],['a','ICN']]
t_ex7 = [['ICN', 'b'],['b','c'],['c','d'],['d','b'],['b','a'],['a','e']]

from cotePracj_copy_22_modulej import makeTicketList # i. 내가만든 모듈의 함수 사용(테스트케이스 자동생성해줌).
num_station=5; least_num_visit = 10
# ticketList = makeTicketList(num_station, least_num_visit)

import random
# random.seed(0)
# shuffled = random.sample(ticketList, len(ticketList))
shuffled = random.sample(t_ex7, len(t_ex7))
print('shuffled:',shuffled)
ret = solution(shuffled)
print('j) answer:{}st, {}'.format(len(ret),ret))




# def solution(tickets):
#     num_t = len(tickets)
#     seq=[["", "ICN"]]
#     popped_list = []
#     while len(seq)-1!=num_t:    
#         last_st = seq[-1][1]
#         next_t_list = sorted([t for t in tickets if t[0]==last_st], key=lambda x: x[1])
#         if len(popped_list)!=0 and popped_list[-1] in next_t_list:
#             next_t_list.remove(popped_list[-1])
#         if len(next_t_list)>0: 
#             seq.append(next_t_list[0])
#             tickets.remove(next_t_list[0])
#             if next_t_list[0] in popped_list:
#                 popped_list.remove(next_t_list[0])        
#         else:
#             popped = seq.pop(-1)
#             tickets.append(popped)
#             popped_list.append(popped)
    
#     return ['ICN'] + [i[1] for i in seq[1:]]