from itertools import product
prodTup_list = list(product(range(1,10), repeat=3)) # [(1,1,1), (1,1,2), (1,1,3), ...]
prod_list = []
for prodTup in prodTup_list:
    prodStr = ''
    for i in prodTup:
        prodStr += str(i)
    prod_list.append(int(prodStr))
# -> prod_list = [111, 112, 113, ...]

def solution(baseball):
    can_list = [[i,0,0,1] for i in prod_list]
    for base in baseball:
        can_list = retSols(base, can_list)
    return len([i for i in can_list if i[3]==1])   
       
def retSols(base, can_list):  
    can_list = [can for can in can_list if can[3]==1]    
    try_str = str(base[0])
    for Cdx, can in enumerate(can_list):
        for Tdx, t in enumerate(try_str):
            if t in str(can[0]):
                if str(can[0])[Tdx] == t:
                    can_list[Cdx][1] += 1
                else:
                    can_list[Cdx][2] += 1
    for Cdx, can in enumerate(can_list):
        if can[1:3] != base[1:]: can_list[Cdx][3] = 0
        can_list[Cdx][1]=0; can_list[Cdx][2]=0
    return can_list


baseball_ex1 = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]  # ret = 2
