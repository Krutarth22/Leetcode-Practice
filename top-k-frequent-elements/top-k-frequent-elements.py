class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        ans = Counter(nums)
        
        final = ans.most_common(k)
        
        result = []
        
        for i in final:
            result.append(i[0])
        return result