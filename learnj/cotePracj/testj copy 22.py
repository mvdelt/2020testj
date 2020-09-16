
def testf(a, b):
    print('i am testf, ', a, b)


class TestClass:
    def testf(self, a, rec):
        print('hi ',a+str(rec))
        if rec<=10:
            self.testf(a, rec+1)
            testf(a, rec+1)

tc = TestClass()
tc.testf('jun', 0)