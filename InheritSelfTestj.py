class A(object):
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        # print(self.in1, self.in2)
    def fct1(self, a, b):
        ins_of_self = type(self)(a, b)
        return ins_of_self
    def fct2(self):
        print(self, self.in1, self.in2)

insA = A(11,22)
insA.fct2()

insOfSelf = insA.fct1(111,222)
insOfSelf.fct2()

class B(A):
    pass

insB = B(55,66)
print(insB)
insB.fct2()

insOfSelf2 = insB.fct1(555,666)
print(insOfSelf2)
insOfSelf2.fct2()

class C(B):
    pass

insC = C(88,99)
print(insC)
insC.fct2()

insOfSelf3 = insC.fct1(888,999)
print(insOfSelf3)
insOfSelf3.fct2()

class D(C):
    def fct2(self):
        print('im fct2 in {}, ins of class D'.format(self))
        super().fct2()

insD = D(0,1)
print(insD)
insD.fct2()
