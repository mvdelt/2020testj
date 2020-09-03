# i. cotePracj copy 22.py 파일에서 지금 요 파이썬파일(모듈)을 임포트시키게 만들엇음.

# i. 2020.08.02.일욜오전.
# 프로그래머스 여행경로 테스트케이스 자동생성기 만들어보려함.
# -문제 설명-
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. *항상 ICN 공항에서 출발*합니다.
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
# -제한사항-
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 *모두 사용해야* 합니다.
# 만일 가능한 경로가 2개 이상일 경우 *알파벳 순서*가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.



import random
def makeStList(numSt, chars='abcdefghijklmnopqrstuvwxyz'):
    assert len(chars)==len(set(chars)), 'j) error! maybe there are redundunt character in given chars'
    assert numSt>=3 and numSt<=1000, 'j) 주어진 공항 수는 3개 이상 10,000개 이하여야함'
    stList = ['ICN']
    while len(set(stList))!=numSt:
        stName = ''.join(random.sample(chars, 3)).upper() # i. 알파벳 고를때 중복해서고르는건 안하고있는데, 걍 일케 하자.
        stList.append(stName)
    # print('stList:',list(set(stList)))
    return list(set(stList))


# stList = makeStList(numSt, alphabets)
# print('stList:',stList) # i. 잘 작동.

def makeVisitSeq(stList, leastNumVisit): # i. 총 방문횟수는 적어도 leastNumVisit 이상이 되도록.
    assert leastNumVisit>=len(stList), 'j) 최소방문횟수는 공항수 이상으로 정해줘야함!'
    visitSeq = ['ICN']
    # while len(visitSeq)<leastNumVisit or len(set(visitSeq))!=len(stList): # i. 아랫줄조건과 동일할거임. 아랫줄처럼작성하는게 이해하기쉬울듯.
    while not (len(visitSeq)>=leastNumVisit and len(set(visitSeq))==len(stList)): # i. while !(내가원하는조건) ->이렇게쓰면 내가원하는조건이 될때까지 루프계속도는거지.
        stList_copy = stList[:] # i. 파이썬에서는 while 이나 for loop 등은 scoping시 적용되는 블록이 아니라서, stList=stList[:] 라고해도 에러는 안나지만, 이러면 복사하려는 의미가 없어지지.
        stList_copy.remove(visitSeq[-1])
        visitSeq.append(*random.sample(stList_copy, 1))
    print('j) visitSeq:{}st, {}'.format(len(visitSeq), visitSeq))
    # print('set(visitSeq):',set(visitSeq))
    return visitSeq

def makeTicketList(num_station, least_num_visit):
    station_list = makeStList(num_station)
    visit_sequence = makeVisitSeq(station_list, least_num_visit)
    ticketList = []
    for idx in range(len(visit_sequence)):
        if idx==0: continue
        ticket = visit_sequence[idx-1:idx+1] # i. index slicing 할때는 인덱스 범위 벗어나도 괜춘.
        ticketList.append(ticket)
    print('ticketList:',ticketList)
    return ticketList

if __name__=='__main__':
    numSt_input = input('j) How many airports(stations) do you wanna create?')
    leastNumVisit_input = input('j) plz set the least number of visiting:')
    # print(type(numSt_input)) # i. <class 'str'> ->정수로바꿔줘야함.
    makeTicketList(int(numSt_input), int(leastNumVisit_input))

