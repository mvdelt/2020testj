# i. leetcode 'Reverse Linked List' 문제. iterative, recursive 두방법 모두로 풀어봣음.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# i. iterative 솔루션.###########################################
class Solution_iter:
    def reverseList(self, head: ListNode) -> ListNode:
        # nextNode=head
        # while not (nextNode.next==None):
        #     nextNode = nextNode.next
        # nextNode.next = head
        
        if head == None:
            return None
        
        head.before='origHead'
        currentNode=head
        while not (currentNode.next==None):
            currentNode.next.before=currentNode
            currentNode = currentNode.next        
        # i. 현재 currentNode는 맨마지막노드임.
        
        retj = currentNode
        
        while not (currentNode.before=='origHead'):
            currentNode.next = currentNode.before
            currentNode = currentNode.next
        # i. 현재 currentNode는 맨첨노드임.
        currentNode.next=None
        
        return retj
###################################################################
        
        # currentNode=head
        # while not ():
        #     nextNode = currentNode.next
        #     nextnextNode = nextNode.next
        #     nextNode.next = currentNode
        #     currentNode = nextNode
        

# i. recursive 솔루션.
class Solution:
    def reverseList(self, head: ListNode)->ListNode:
       
        if head==None:
            return None
    
        if head.next == None:
            if hasattr(head, 'before'):
                head.next = head.before
            return head
        
        head.oriNext = head.next
        head.next.before = head
        if hasattr(head, 'before'):
            head.next = head.before
        else:
            head.next = None
        return self.reverseList(head.oriNext)
    
    
    
    
        ###############################
    
#         if head.oriNext == None:
#             head.next.oriNext = head.next.next
#             head.next.next = head           
            
#             head.oriNext = head.next
#             head.next = None
#             self.reverseList(head.oriNext)
        
#         if head.oriNext == None:
#             return head
#         head.oriNext.oriNext = head.oriNext.next
#         head.oriNext.next = head      

#         if head.oriNext.oriNext == None:
#             return head.oriNext
        
#         self.reverseList(head.oriNext)

        
        
        
        
        
        
        
        
        
        