
# i. 2020.05.20.수욜낮.) 이제 __setattr__ 가 뭔지, 무한리컬젼을 막기위해 super().__setattr__ 써주는것 등등 다 이해완료. 덤으로 try except 구문에서 error 처리하는것도 더 확실히 이해완료.
# __setattr__ 를 커스텀정의해주면, attribute 를 셋 해줄때 (a.key = value 방식으로 하든, setattr(a,key,value)방식으로하든) __setattr__ 가 실행됨!! (stackoverflow 어느답변: "__setattr__ is called for *all* attribute setting.")
# 거기서 맘대로 처리할거 처리하도록 정의해주고, 셋 해줄때는 super().__setattr__ 를 사용해서 무한리컬젼 발생하지 않도록 해주면 됨.

class A:
    def __init__(self):
        print("j) class A is initialezed as an object")
    def __setattr__(self, key, val):
        try:
            # i. 요기서 만약 key 가 없으면 AttributeError 발생하고, 그러면 요아래 exept AttributeError: 블럭으로 이동하는거지.
            # 만약 key 가 존재하면 아래 assert 조건 체크해서 조건안맞으면 AssertionError를 띄우거나, 조건맞으면 아무일도 안하는거지(이미 key 와 그에해당하는 값이 존재하고, 그 값이 새로 넣어주려는 값과 동일하니까.).
            oldval = getattr(self, key) 
            print('oldval:',oldval)
            print('val:',val)
            assert oldval == val, (
                "Attribute '{}' in the metadata of '{}' cannot be set "
                "to a different value!\n{} != {}".format(key, "thisIsTestj", oldval, val)
            )
        except AttributeError:
            key = key + "_kk88"
            super().__setattr__(key, val)
        except:
            print('some error occured ......!! j')
            raise

a = A()

a.keytestj = "yoyokeytestj"
print(a.__dict__)
print(a.keytestj_kk88)
# print(a.keytestj) # AttributeError: 'A' object has no attribute 'keytestj'

a.keytestj_kk88 = 'yoyokeytestj' # i. 기존값과동일하므로 아무일도안일어남.
print(a.__dict__)
a.keytestj_kk88 = 'yoyokeytestj2' # i. 기존값과 다르므로 AssertionError 발생.
print(a.__dict__)
