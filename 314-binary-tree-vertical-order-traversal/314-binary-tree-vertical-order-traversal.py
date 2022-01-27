# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        cols = defaultdict(list)
        
        s = deque([(root, 0)])

        
        if not root:
            return []
        
        while s:
            
            node, col = s.popleft()
            
            cols[col].append(node.val)
            
            if node.left:
                s.append((node.left, col-1))
                
            if node.right:
                s.append((node.right, col+1))
                
        return [cols[k] for k in sorted(cols.keys())]