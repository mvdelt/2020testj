# i. LeetCode 미디엄급 문제 Construct Binary Tree from Preorder and Inorder Traversal 내 솔루션. 억셉된거임.
# 내풀이 아주 만족스러움. 설계하는데 삼사십분쯤 걸렸는데, 구현이넘오래걸렷음;; 구현까지하지 한시간넘어감;;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(preorder)==0 and len(inorder)==0:
            return None
        
        root = preorder[0]
        inorder_root_idx = inorder.index(root)
        
        left_inorder = inorder[:inorder_root_idx]
        right_inorder = inorder[inorder_root_idx+1:]
        
        if len(right_inorder)!=0:
            preorder_rightRoot_idx = min([preorder.index(i) for i in right_inorder])
        else:
            preorder_rightRoot_idx = len(preorder)
        
        left_preorder = preorder[1:preorder_rightRoot_idx]
        right_preorder = preorder[preorder_rightRoot_idx:]
                
        return TreeNode(val=root, left=self.buildTree(left_preorder, left_inorder), right=self.buildTree(right_preorder, right_inorder))
