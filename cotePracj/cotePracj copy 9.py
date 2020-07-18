import itertools

def solution(numbers):    
    pList = list(itertools.permutations(numbers))
    return str(max([int(''.join(map(str,p))) for p in pList]))


numlist_ex1 = [3, 30, 34, 5, 9]
res = solution(numlist_ex1)
print(res)