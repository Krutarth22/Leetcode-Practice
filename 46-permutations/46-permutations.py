class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = permutations(nums)
        
        final = []
        
        for i in ans:
            final.append(list(i))
            
        return final