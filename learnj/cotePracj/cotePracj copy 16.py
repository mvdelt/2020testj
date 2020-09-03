import itertools

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

# ret=powerset([1,2,3,4,5])

# count = 0
# for i in powerset([1,2,3,4,5]):
#     if sum(i)%2==0: count+=1
#     print(i,sum(i), count)



from itertools import product
def solution2(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

# nums = [1,1,1,1,1]; target=3
# ret=solution2(nums,target)
# print(ret) 

tup_list = [(1,2), (3,4), (5,6)]
# list2 = ['a','b']
for i in product(*tup_list):
    print(i)