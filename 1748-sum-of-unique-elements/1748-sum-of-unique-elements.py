class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        
        ans = Counter(nums)
        
        for i in ans:
            
            if ans[i] == 1:
                result.append(i)
                
        return sum(result)