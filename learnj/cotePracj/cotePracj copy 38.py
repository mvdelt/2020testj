# i. 2020.08.21.금욜) leetcode 의 Binary Tree Zigzag Level Order Traversal 문제 내솔루션. accept됏음.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        0. root에서 .lev에 현재레벨 저장, 자식lev도 설정.
        1. 자식노드들의 .lev에 레벨(현재lev+1) 저장. 
        2. dict에 lev을 키, val을 밸류로 저장.
        3. dict 완성됏으면, 홀/짝에 따라 뒤집어서~~ 끝.
        """
        if not root:
            return []        
        
        levdict = {}
        
        root.lev = 0
        
        def helper(node: TreeNode):
            """
            1. dict에 lev, val 저장.
            2. 자식노드들의 lev 셋팅.            
            """
            if not node:
                return
            
            if node.lev not in levdict:
                levdict[node.lev]=[]
            levdict[node.lev]+=[node.val]

            if node.left:
                node.left.lev = node.lev + 1
            if node.right:
                node.right.lev = node.lev + 1

            helper(node.left)
            helper(node.right)
            
            return        
        
        helper(root)
        
        ret = []
        for lev in levdict:
            if lev%2==0:
                ret+=[levdict[lev]] # i. append 대신에 걍 이렇게 해줘봄. 3개이상을 합칠때는 append 보다 이렇게 +로 더해주는게 좋을듯.
            else:
                ret+=[levdict[lev][::-1]]
        return ret        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        