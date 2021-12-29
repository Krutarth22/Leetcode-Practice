class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = min(nums)
        
        big = max(nums)
        result = []
        for i in range(1,small+1):
            
            if small % i == 0 and big % i == 0:
                
                result.append(i)
                
        return result[-1]