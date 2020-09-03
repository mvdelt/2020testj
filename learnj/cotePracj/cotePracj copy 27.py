# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    depthSet = set()
    def maxDepth(self, root: TreeNode) -> int:
        # print('j) type(root):',type(root))
        # print('j) type(TreeNode):',type(TreeNode))
        if type(root)!=TreeNode:
            print('j) 1st root is not TreeNode')
            return 0
        self.writeDepth(root)
        return max(self.depthSet)
    
    def writeDepth(self, node: TreeNode):
        if not hasattr(node, 'depth'):
            node.depth = 1
        self.depthSet.add(node.depth)

        if hasattr(node, 'left') and type(node.left)==TreeNode:
            node.left.depth = node.depth + 1
            self.writeDepth(node.left)
        else:
            pass
        if hasattr(node, 'right') and node.right!=None:            
            node.right.depth = node.depth + 1
            self.writeDepth(node.right)
        else:
            pass

rootNodej = TreeNode()
sol = Solution()
retj = sol.maxDepth(rootNodej)
print(retj)