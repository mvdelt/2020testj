# def solution(N, number):
    
#     if N==number:
#         return 1  

#     # 더하기.
#     if number-N > 0
#         plus = solution(N, number-N) +1
    
#     # 곱하기.
#     if number%N == 0:
#         mul = solution(N, number/N) +1
        
#     # 빼기.
    
#     solution(N, number+N) +1
#     if N-number>=0:
#         minus = solution(N, N-number) +1
    
#     # 나누기.
#     devide1 = solution(N, number*N) +1
#     if N%number==0:
#         devide2 = solution(N, N/number) +1
    
#     # 이어붙이기.
#     if number-N>0 and (number-N)%10==0:
#         attach = solution(N, (number-N)/10) +1
    
    
#     answer = 0
#     return answer


def solution(N, number):

    def sol_inner(N, number, ncall):
        
        if N==number:
            return 1  

        
        # if number>1000 or number<-1000:
        #     return float('inf')

        if ncall>8:
            return float('inf')


        cand = []

        # 더하기.
        plus = sol_inner(N, number-N, ncall+1) +1
        cand.append(plus)
        
        # 곱하기.
        mul = sol_inner(N, number/N, ncall+1) +1
        cand.append(mul)
            
        # 빼기.    
        minus1 = sol_inner(N, number+N, ncall+1) +1
        cand.append(minus1)
        minus2 = sol_inner(N, N-number, ncall+1) +1
        cand.append(minus2)
        
        # 나누기.
        devide1 = sol_inner(N, number*N, ncall+1) +1
        cand.append(devide1)
        if number!=0:
            devide2 = sol_inner(N, N/number, ncall+1) +1
            cand.append(devide2)
        
        # 이어붙이기.
        if len(set(str(number)))==1 and list(set(str(number)))[0]==str(N):
            # print(f'이어붙이기! call:{ncall}')
            attach = sol_inner(N, (number-N)/10, ncall+1) +1
            cand.append(attach)

        # if len(cand)!=6:
        #     print('cand:',cand)
        return min(cand)
    
    ret = sol_inner(N, number, 1)
    if ret>8:
        return -1
    else:
        return ret

N, number = 4, 27
ret = solution(N, number)
print(ret)