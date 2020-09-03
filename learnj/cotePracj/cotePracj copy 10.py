import itertools

def solution(numbers):    
    pList = list(itertools.permutations(numbers))
    print(pList[0])
    # print(''.join(map(str,pList[0])))
    # print(''.join(str(x) for x in pList[0]))
    print(map(str,pList[0]))
    print(''.join(map(str,pList[0])))


numlist_ex1 = [3, 30, 34, 5, 9]
res = solution(numlist_ex1)
print(res)