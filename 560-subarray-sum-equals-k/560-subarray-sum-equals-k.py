class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        d = {}
        
        d[0] = 1
        
        s = 0
        
        count = 0
        
        for i in range(len(nums)):
            
            s+=nums[i]
            
            if s - k in d:
                
                count+=d[s-k]
                
            if s in d:
                
                d[s] +=1
                
            else:
                
                d[s] = 1
                
                
        return count