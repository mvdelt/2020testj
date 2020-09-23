
def inf_seq():
    num=0
    while num<3:
        yield num
        num+=1
    return 'hihi'

print(inf_seq)   # <function inf_seq at 0x000001DCDB8C7AF8>
genObj = inf_seq()  
print(genObj)   # <generator object inf_seq at 0x0000020CD3404E48>
print(next(genObj))   # 0
print(next(genObj))   # 1
print(next(genObj))   # 2
# print(next(genObj))   # StopIteration: hihi

iteratorj = iter([1,2,3,4])
print(iteratorj)         # <list_iterator object at 0x00000160D182F748>
iteratorj2 = iter([1,2,3,4])
print(iteratorj2)        # <list_iterator object at 0x00000160D182F088>
print(iter([1,2,3,4]))   # <list_iterator object at 0x00000160D182F208>
print(iter([1,2,3,4]))   # <list_iterator object at 0x00000160D182F208>
print(iter([1,2,3,4]))   # <list_iterator object at 0x00000160D182F208>

# print(zip([1,2],[3,4,5],['a','b','c']))
# print(list(zip([1,2],[3,4,5],['a','b','c'])))
# print(set(zip([1,2],[3,4,5],['a','b','c'])))

# zipObj = zip([1,2],[3,4,5],['a','b','c'])
# a,b=zipObj
# print(a,b)

# print('hi') if True else 'nothing'