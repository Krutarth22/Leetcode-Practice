class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        l, h = 0, len(nums) # add 1 more, low-end, dont worry m never be this one.
        while l<h:
            m=l+h>>1  # low end mid
            missed = nums[m] - (m + nums[0])
            if missed<k: l=m+1 # if missed less than k, l must be greater than m. 
            else:h=m
        return (l-1 + nums[0]) + k # before the insert location + k missing 
                