# Detectron2 관련 테스트(요건 Detectron2의 직접적 코드는 아니고 Detectron2에서 사용하고있는 fvcore라는것의 코드에서 가져온거지만).

# 알게된점: 타입힌트 ( 콜론 뒤에 타입 써주는 그런거) 는 그냥 아무 강제성이 없네!!! 
# 여기 오타로 : list 라고 해줫지만, 사실 딕셔너리가 들어가야 작동하며, 딕셔너리가 들어가도 전혀 문제가 없음.

from abc import ABCMeta

class Transform(metaclass=ABCMeta):
    def _set_attributes(self, params: list = None): # i. list가 아니라 dict여야 맞는데, 이렇게해도 작동엔 아무문제없다는거지 내말은.
        """
        Set attributes from the input list of parameters.

        Args:
            params (list): list of parameters. # i. 요 설명도 오타고. list대신 dict로 바꿔줘야함. 
        """

        # if params:
        for k, v in params.items():
            if k != "self" and not k.startswith("_"):
                setattr(self, k, v)
                # print('k,v:',k,v)
        print('in _set_attributes, locals():',locals())

# _set_attributes({'bb':333, 'ccc': 4444})
# _set_attributes([3,4,5,6,7])

Tj = Transform()
Tj._set_attributes({'bb':333, 'ccc': 4444, 'hihijjj':99})
print('Tj.__dict__:',Tj.__dict__)
print(dir(Tj))
print('Tj.bb:',Tj.bb)
print('in global, locals():',locals())

