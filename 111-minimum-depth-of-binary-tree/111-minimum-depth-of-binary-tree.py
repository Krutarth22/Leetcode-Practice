# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        if root.left is None:
            return 1 + self.minDepth(root.right)
        
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        
        else:
            
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        