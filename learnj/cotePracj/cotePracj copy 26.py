# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    depthSet = set()
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        self.writeDepth(root)
        return max(self.depthSet)
    
    def writeDepth(self, node: TreeNode):
        if not hasattr(node, 'depth'):
            node.depth = 1
        self.depthSet.add(node.depth)

        if node.left!=None:
            node.left.depth = node.depth + 1
            self.writeDepth(node.left)
        else:
            pass
        if node.right!=None:            
            node.right.depth = node.depth + 1
            self.writeDepth(node.right)
        else:
            pass

rootNodej = TreeNode()
sol = Solution()
retj = sol.maxDepth(rootNodej)
print(retj)