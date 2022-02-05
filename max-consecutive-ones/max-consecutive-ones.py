class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ones = 0
        
        for i in nums:
            
            if i == 1:
                
                count+=1
                
                ones = max(count, ones)
                
            else:
                
                count = 0
                
        return ones