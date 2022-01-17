class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        result = {}
        
        for i, num in enumerate(nums):
            
            difference = target - num
            
            if difference in result:
                
                return [i,result[difference]]
            
            else:
                
                result[num] = i
            
            