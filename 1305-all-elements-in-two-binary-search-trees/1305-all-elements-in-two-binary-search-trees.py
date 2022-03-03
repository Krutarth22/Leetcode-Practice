# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder(root, arr):
            
            if not root:
                return
            
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
            
        arr1 = []
        arr2 = []
        
        inorder(root1, arr1)
        inorder(root2, arr2)
        
        result = []
        index1, index2 = 0, 0
        
        l1 = len(arr1)
        l2 = len(arr2)
        
        while index1 < l1 and index2 < l2:
            
            if arr1[index1] < arr2[index2]:
                
                result+= [arr1[index1]]
                index1+=1
                
            else:
                
                result += [arr2[index2]]
                index2+=1
                
        return result + arr1[index1:] + arr2[index2:]