# empty dictionary
my_dict = {}
print(my_dict)

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)


# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)


# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)


# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)


# AttributeError: 'dict' object has no attribute 'testjun'
# my_dict.testjun = 'heyjun'

# 위처럼하면 에러뜨고, 아래처럼 하면 됨.
# 위처럼 하게 하려면, 딕셔너리를 상속하는 새로운 클래스 만든담에 __setattr__인가 그거 해줘야할거임. 맞네 밑에서 해보니.
my_dict['testjun'] = 'heyjun'
print(my_dict)

class NewDictj(dict):
    def __init__(self,  **kwargsj):
        super().__init__( **kwargsj)
    def __setattr__(self, k, v):
        self[k] = v
    def __getattr__(self, k):
        return self[k]

# ndj = NewDictj({'himan':'greatyo', 'dudu':'gengen', 'agej':18})
ndj = NewDictj(himan='greatyo', dudu='gengen', agej=18)
print(ndj)

ndj.newGenJun = 'you are genius j'
print(ndj)

ndj.minij = NewDictj()
print(ndj)
ndj.minij.hohoj = "i am hohoj"
print(ndj)


class Simplej:
    pass

sj = Simplej()
sj.hahaman = 'testhahaman'
print(sj.__dict__)
print(sj.hahaman)

# TypeError: 'Simplej' object does not support item assignment
# sj['hahaman2'] = 'testhahaman2'
