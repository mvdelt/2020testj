
# def vs(a,b):
#     len_a = len(a)
#     len_b = len(b)
#     return False if len_a > len_b
#     b2 = b[:len_a]
#     return True if a == b2

# def putZeros(i):
#     return (i + '0'*(20-len(i)))

# i. 내가 만든 솔루션. 구글링은 했음.
#   -> ㅡㅡ 아놔 미치겟네;; sort또는sorted 쓸때 string 대상으로 쓰면 내가원하는대로 정렬되네 ㅡㅡ;;;; 괜히 헛고생;;;;
#   -> 첨에 인풋예시 복붙하니까 스트링이 걍 int로 복붙돼서(이유는 모름; 다른건 또 스트링으로 복붙되는데;;) 
#       int대상으로 sort 했더니 숫자 크기대로 정렬돼서 내가원하는대로 안되는줄알앗는데;;; str대상으로 정렬햇으면 되는거엿는데;;;
#       암튼 내가 놓친거임. str 대상으로 정렬햇을때 숫자크기대로 정렬이 안돼야 정상이자나!!!!! 내부적으로 int로 바꿔 정렬해주지 않는이상;;
import operator
def solution(pn_list):
    tuplist = [(i, (lambda x: x + '0'*(20-len(x)))(i), len(i)) for i in pn_list]
    tuplist.sort(key = operator.itemgetter(1,2))
    print(tuplist)
    for i in range(len(pn_list)-1):
        if tuplist[i+1][0].startswith(tuplist[i][0]):
            return False
    return True
        

pn_list_ex1 = ['12','123','1235','567','88']
pn_list_ex2 = ["123", "456", "789"]
res = solution(pn_list_ex1)
print(res)