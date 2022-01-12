# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ans = []
        
        queue = [root]
        
        while queue:
            
            tree = queue.pop(0)
            
            if tree.right:
                queue.append(tree.right)
                if not tree.left:
                    
                    ans.append(tree.right.val)
                    
            if tree.left:
                
                queue.append(tree.left)
                
                if not tree.right:
                    
                    ans.append(tree.left.val)
                    
        return ans