class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        
        ans = Counter(nums1)
        
        for i in nums2:
            
            if ans[i] > 0:
                result.append(i)
                ans[i]-=1
                
        return result