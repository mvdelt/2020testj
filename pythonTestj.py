class JunClass:
    def method1(self):
        print('im method1')
    def method2(self):
        print('im method2')
    def method3(self):
        print('im method3')
    def method4(self):
        self.method1()
    def method5(self):
        JunClass.method2(self)

jc = JunClass()

jc.method1()
jc.method2()
jc.method3()
jc.method4()
jc.method5()
