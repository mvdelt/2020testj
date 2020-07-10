

class TestClass():
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        print('self.arg1:',self.arg1)
        print('id of self.arg1:',id(self.arg1))
        print('id of arg1:', id(arg1))
        self.arg2 = arg2
        print('self.arg2:',self.arg2)
        
        arg1 = [2,4,5]
        print('self.arg1:',self.arg1)
        print('id of self.arg1:',id(self.arg1))
        print('id of arg1:', id(arg1))

        arg2 = 'blahjjj'
        print('self.arg2:',self.arg2)

tc = TestClass('arg1yeah', 3344)