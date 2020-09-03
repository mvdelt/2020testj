par = ["a", "b", "c", "d", "e", "c", "d", "c", "z", "y", "x", "andy"]
com = ["a", "b", "c", "d", "e", "c", "d", "c", "z", "y", "x"]

def solution(par, com):
    num_com = len(com)
    com_dict = {com[i]: i for i in range(num_com)}
    print('com_dict:',com_dict)
    for p in par:
        if p in com_dict:
            del com_dict[p]
        else:
            return p

res = solution(par, com)
print('not finished:',res)

for i in zip(par,com):
    print(i)