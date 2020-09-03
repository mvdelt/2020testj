# i. 2020.09.03. 파이썬 람다 복습. 예전에 이미 공부해서 알았던건데, 까먹어서 다시 복습후 이해완료.

class FctBox():

    def __init__(self):
        self.box = []

    def put(self, fctPt):
        self.box+=[fctPt]

    def exc(self):
        for fctPt in self.box:
            print(fctPt())


fbox = FctBox()
for s in ['I', 'am', 'sorry']:
    fbox.put(lambda: s)  # i. 이렇게 하면 람다가 호출되는시점에서의 s를 사용하게됨. 

for s in ['but I', 'love', 'you']:
    fbox.put(lambda x=s: x+'★')  # i. 해결책1) 디폴트값 이용. (여기서 람다의 인풋인자 x 의 디폴트값을 s로 한거지. x=s 요부분에서.)

for s in ['for', 'real']:
    fbox.put((lambda x: lambda: x+'♥')(s))  # i. 해결책2) 기존 람다를 랩핑하는 새로운 람다를 만들어서, 그냥 for문의 각 이터레이션마다 이 랩핑람다를 곧바로 호출해줘버림.


print(f'fbox.box: {fbox.box}')

fbox.exc()