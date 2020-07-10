from types import SimpleNamespace

import random

class DataBag(SimpleNamespace):

    button1 = 'button1 - blue, shiny, big.'

    def choice(self):
        items = self.__dict__.items()
        print('data_bag.button1:',self.button1)
        print('Databag.__dict__:',self.__dict__)
        print('from DataBag-choice, items:',items)
        return random.choice(tuple(items))

data_bag = DataBag(a=1, b=2, c=3, d=55, e=8989)
data_bag.fafafa = 'fafafa555'
print('Genesis - data_bag.__dict__:',data_bag.__dict__)
print('Genesis - DataBag.__dict__:',DataBag.__dict__)

print('data_bag:',data_bag) # DataBag(a=1, b=2, ...)
print('-----------------------')
print('data_bag.choice():',data_bag.choice()) # ex: (b, 2)

# print('Databag.__dict__:',data_bag.__dict__)

