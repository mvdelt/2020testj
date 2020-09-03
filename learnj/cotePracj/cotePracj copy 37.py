# i. 2020.08.20.목욜.) LeetCode 의 Odd Even Linked List 문제 내가푼솔루션. accept된 솔루션임.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        # 인풋으로 아예 노드가 없는경우가 들어올경우.
        if head==None:
            return None
        
        # 총 노드 갯수 1개뿐일경우, 그냥 이 노드(head)를 리턴.
        if head.next==None:
            return head
        
        # 맨처음 노드(head)를 가리키는변수 만듦. 나중에 이놈을 리턴하려고.
        ret = head
        
        # 2nd ln 만들기.
        second_ln = head.next
        
        # seq를 1로 지정.
        head.seq = 1      
        
        while True:
            
            # if next next 가 None 일때, (총 노드갯수 2개밖에 없을때도 커버됨.)
            if head.next.next==None:            
                # i) 현재 seq가 홀수면 2nd ln 으로.
                #    마지막노드(seq짝수) 의 next는 이미 None으로 되어잇어서 건들필요없음.
                if head.seq%2==1:                    
                    head.next = second_ln                
                # ii) 현재 seq가 짝수면 next갓다가 2nd ln으로.
                #     지금현재노드가 마지막노드이므로 next를 None으로 해줘야함.
                else:
                    head.next.next = second_ln
                    head.next = None
                break
                
            # 다음꺼(~>), 수정된 다음꺼(-->) 만들기.
            head.next2 = head.next
            head.next = head.next.next
            # 다음꺼의 seq값 정해주기.
            head.next2.seq = head.seq + 1
            # 반복문을 위해 next를 새로운 head로 해줌.
            head = head.next2
            
        return ret
        