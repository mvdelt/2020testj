def solution(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        # print(hash(part))
        temp += hash(part)
    print(dic)

    dic_com = {}
    for com in completion:
        dic_com[hash(com)] = com
        temp -= hash(com)
    print(dic_com)
    answer = dic[temp]

    return answer

par = ["a", "b", "c", "d", "e", "c", "d", "c", "z", "y", "x", "andy", "gaga","haha",]
com = ["a", "b", "c", "d", "e", "c", "d", "c", "z", "y", "x","gaga","haha"]

res = solution(par,com)

print(res)