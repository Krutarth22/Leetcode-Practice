class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left = []
        
        right = []
        
        result = []
        
        value = 1
        
        for i in range(len(nums)):
            left.append(value)
            
            value*=nums[i]
            
        
        value = 1
        
        for i in range(len(nums)-1, -1, -1):
            
            right.append(value)
            
            value*=nums[i]
            
        right = right[::-1]
        
        
        for i in range(len(nums)):
            result.append(left[i] * right[i])
            
            
        return result
        