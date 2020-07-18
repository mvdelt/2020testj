
def solution_slow(m, n, puddles):
    from itertools import combinations
    def rlist(m, n):
        tot_dir_list = list(range(1,(m-1+n-1)+1))
        r_comb_list = list(combinations(tot_dir_list, m-1))
        rzeros_list = []
        for r_comb in r_comb_list:
            zeros = [0]*len(tot_dir_list)
            for r in r_comb:
                zeros[r-1] = r
            rzeros_list.append(zeros)
        return rzeros_list

    rzeros_list = rlist(m, n)
    # print('before) rzeros_list:',rzeros_list) # i. 여기까진 ok.
    for idx, rzeros in enumerate(list(rzeros_list)):
        gotpud = 0
        for pud in puddles:
            movNum2pud = pud[0]-1 + pud[1]-1
            until_pud = rzeros[:movNum2pud]
            right = len(until_pud)-until_pud.count(0)
            if right == pud[0]-1:
                gotpud+=1
                break
        if gotpud == 1:
            rzeros_list.remove(rzeros)
    # print('after) rzeros_list:',rzeros_list)
    return len(rzeros_list)%1000000007


def solution2(m,n,puds):
    calsol_dict = {} # i. 계산결과 저장해놓기위한 딕셔너리.
    # puds_set = {tuple(p) for p in puds} # i. puds list를 set{tuple} 로 바꿈.
    for pud in puds:
        calsol_dict[tuple(pud)] = 0
    def sol_inner(m,n):
        # i. m,n 둘다 1인경우.
        if m==1 and n==1:
            return 1
        # i. m 또는 n 이 0 인 경우.
        if m==0 or n==0:
            return 0
        # # i. [m,n] 이 물일경우.
        # if (m,n) in puds_set:
        #     return 0
        # i. 기존 기록에서 검색. 기존기록에없으면 계산해서 기록저장후 리턴.
        if (m,n) in calsol_dict:
            return calsol_dict[(m,n)]
        else:
            calsol_dict[(m,n)] = sol_inner(m,n-1) + sol_inner(m-1,n)
            return calsol_dict[(m,n)]
        # return calsol_dict.setdefault((m,n), sol_inner(m,n-1) + sol_inner(m-1,n))
        # i. -> setdefault 함수 검색 엄청느림!!! in 으로 검색하는것보다 훨씬 더 느림. 안쓰는게좋을듯!!!
        #       근데 바로윗줄에서 이미 in 으로 검색을 하면, 아마도 컴파일러?인터프리터?가 그 결과를 저장해놨다가 필요시 다시사용하는듯?
        #       윗줄에서 in 사용하면 아랫줄에서 setdefault 사용해도 안느림.
    return sol_inner(m,n)%1000000007


def solution3(m,n,puds):
    mapj = [[-1]*(n+1) for _ in range(m+1)]
    mapj[1][1] = 1
    mapj[0] = [0]*(n+1)
    for pud in puds:
        mapj[pud[0]][pud[1]] = 0
    for i in range(1,m+1):
        mapj[i][0] = 0
        for j in range(1,n+1):
            if mapj[i][j] == -1:
                mapj[i][j] = mapj[i][j-1]+mapj[i-1][j]      
    return mapj[m][n]%1000000007


        

    






m=4;n=3;puddles=[[2,2]]
# print(list(range(1,(m-1+n-1)+1)))
print(solution_slow(m,n,puddles))
print(solution2(m,n,puddles))
print(solution3(m,n,puddles))