class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def binaryleft(A,x):
            
            left, right = 0, len(A) - 1
            
            while left <= right:
                
                mid = (left+right) / 2
                
                if A[mid] < x:
                    
                    left = mid + 1
                    
                else:
                    
                    right = mid - 1
                    
            return left
                
            
        def binaryright(A,x):
            
            left, right = 0, len(A) - 1
            
            while left <= right:
                
                mid = (left+right) / 2
                
                if A[mid] <= x:
                    
                    left = mid + 1
                    
                else:
                    
                    right = mid - 1
                    
            return right
                
            
        left = binaryleft(nums, target)
        right = binaryright(nums, target)
        
        return [left, right] if left<=right else [-1,-1]
        