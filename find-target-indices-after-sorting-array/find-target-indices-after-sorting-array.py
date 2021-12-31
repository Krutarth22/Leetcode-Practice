class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result =[]
        for index, value in enumerate(nums):
            
            if value == target:
                
                result.append(index)
                
        return result