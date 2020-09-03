# i. 프로그래머스 도둑질 문제(원형으로 배열된 집 털기 문제).

# i. 1) DP(Dynamic Programming) 재귀호출로 풀기. ->호출너무많이해서그런지 프로그래머스서버에서 런타임에러뜸. 스택오버플로인듯.
def solution(money):

# *** v) maxMoney(1) 계산시에는 money[:-1] 이용해야함!
# *** v) memo 이용할것!!
# *** 집 갯수 적을때 고려!!! ->???고려할필요가없을것같은데..
# ***** 아!!! maxMoney(2) 도 계산해야하네!!!!! 난 maxMoney(0), maxMoney(1) 만 비교하면 되는줄ㅋㅋ

    def maxMoney(i, money, memo): # i: i번째 집.
        # i 가 초과할경우.
        if i > (len(money)-1):
            return 0            
        if i in memo:
            return memo[i]
        memo[i] =  money[i] + max(maxMoney(i+2, money, memo), maxMoney(i+3, money, memo))
        return memo[i]
    
    # print(maxMoney(0, money[:-1], {}), maxMoney(1, money, {}), maxMoney(2, money, {}))
    return max(maxMoney(0, money[:-1], {}), maxMoney(1, money, {}), maxMoney(2, money,{}))


money=[2,1,4,5,9]
print('j) sol 1:', solution(money))



# i. 2) 재귀호출 안쓰고 풀기. ->흠... 이건 시간초과네... 더하는거 중복안되게바꿧는데도 시간초과임..

import copy
def solution2(money):
    
    def M(mon):
        print(f'M start, mon:{mon}')
        stack_list = [[(0, mon[0])]]
        # for mdx, m in enumerate(mon):
        for stack in stack_list:            
            for offset in range(2,4):
                # print('stack[-1]:', stack[-1])
                # print('stack_list:', stack_list)
                mdxToAdd = stack[-1][0]+offset
                if mdxToAdd > (len(mon)-1):
                    continue
                stack_copy = copy.deepcopy(stack)
                # print('stack_copy:', stack_copy)
                # print('mdxToAdd:', mdxToAdd)
                stack_copy.append((mdxToAdd, stack_copy[-1][1]+mon[mdxToAdd]))
                stack_list.append(stack_copy)
        
        # sums=[]
        # for stack in stack_list:
        #     s=0
        #     for i in stack:
        #         s+=i[1]
        #     sums.append(s)

        # print(f'M fin, sums:{sums}')
        return max([stack[-1][1] for stack in stack_list])  

    return max(M(money[:-1]), M(money[1:]), M(money[2:]))


money=[2,1,4,5,9]
print('j) sol 2:', solution2(money))


# i. 3) 다른사람들 풀이 참고해서 다시.
def solution3(money):
    
    maxMon = [0]*len(money)  # maxMon[i]: i까지의 머니 합의 최댓값.
    maxMon[0] = money[0]
    maxMon[1] = max(money[0], money[1])
    # for mdx, m in enumerate(money):
    
    # 1. 마지막집은 뺀 경우.
    for i in range(2, len(money)-1):
        maxMon[i] = max(maxMon[i-2]+money[i], maxMon[i-1])    
    exceptLast = maxMon[-1]

    # 2. 마지막집 포함하고 첫집 뺀 경우.
    maxMon[0]=0
    maxMon[1]=money[1]
    for i in range(2, len(money)):
        maxMon[i] = max(maxMon[i-2]+money[i], maxMon[i-1])    
    exceptFirst = maxMon[-1]

    return max(exceptLast, exceptFirst)
    
    # (1,2 두 경우로 모두 커버됨.)

money=[2,1,4,5,9]
print('j) sol 3:', solution3(money))
        