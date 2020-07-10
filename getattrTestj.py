class A:
    def __getattr__(self, name):
        return ('hahaha-'+name)

    def __getattribute__(self,name):
        return ('jajaja-'+name)
    

a = A()

a.ace = 'ace value'

print(a.ace)
print(a.ace2)
print(a.__dict__)
