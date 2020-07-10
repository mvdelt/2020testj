# i. python 의 filter 이해완료. 2020.06.15.

listj = [3,6,True,12,15,16,17,19,False,False,21,False,False]
print(filter(None,listj))
def filterfctj(el):
    if el%3==0:
        return True
    else:
        return False

evalImgs = [e for e in filter(None,listj)]
evalImgs2 = [e for e in filter(filterfctj,listj)]

print(evalImgs)
print(evalImgs2)
