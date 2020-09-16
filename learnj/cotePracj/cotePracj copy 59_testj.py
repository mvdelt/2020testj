
import collections

# deque: double-ended queue 의 줄임말.

deq = collections.deque(['a','b','c'])
deq2 = collections.deque(['a','b','c'])

deq.extendleft('defg')
print(deq) # deque(['g', 'f', 'e', 'd', 'a', 'b', 'c'])
deq.extend('defg')
print(deq) # deque(['g', 'f', 'e', 'd', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])

deq2.appendleft('defg')
print(deq2)
deq2.append('defg')
print(deq2)

