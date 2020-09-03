# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def l2num(l: ListNode) -> int:
            numli=[]
            while not l==None:
                numli.append(l.val)
                l = l.next            
            # return int(numli[::-1])
            return int(''.join([str(i) for i in numli[::-1]]))
        
        def num2l(num: int) -> ListNode:
            numstrlist = list(str(num))
            lastdigit = int(numstrlist.pop())
            fl = l = ListNode(lastdigit)            
            while not len(numstrlist)==0:
                lastdigit = int(numstrlist.pop())
                
                # i. this doesn't work!!!!!! WHY??????
                l = l.next = ListNode(lastdigit)

                # # i. this works well.
                # l.next = ListNode(lastdigit)
                # l = l.next
                
                # # i. this works well ,too.
                # tmp = ListNode(lastdigit)
                # l.next = tmp
                # l = tmp    
                                
            return fl
        
        return num2l(l2num(l1)+l2num(l2))


def num2l(num: int) -> ListNode:
    numstrlist = list(str(num))
    lastdigit = int(numstrlist.pop())
    fl = l = ListNode(lastdigit)        
    print('.. fl:', fl)
    print('.. l.next:', l.next)
    print('.. l:', l)        
    while not len(numstrlist)==0:
        lastdigit = int(numstrlist.pop())
        
        # i. this doesn't work!!!!!! WHY??????
        # -> 아래의 잘 작동하는경우의 프린트출력결과랑 다름!!!
        # -> 프린트 출력시점에선 l.next가 None이어야하는데 그렇게안됨!! 
        l = l.next = ListNode(lastdigit)
        print('fl:', fl)
        print('l.next:', l.next)
        print('l:', l)

        # # i. this works well.
        # l.next = ListNode(lastdigit)
        # l = l.next
        # print('fl:', fl)
        # print('l.next:', l.next)
        # print('l:', l)
        
        # # i. this works well ,too.
        # tmp = ListNode(lastdigit)
        # l.next = tmp
        # l = tmp    
        # print('fl:', fl)
        # print('l.next:', l.next)
        # print('l:', l)


    return fl

ret = num2l(378)
print(ret.val)
print(ret.next)
# print(ret.next.next.val)

# sol = Solution()
# sol.addTwoNumbers