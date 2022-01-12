class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ix = {i : n for i, n in enumerate(nums) if n}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        
        a,b = self.ix, vec.ix
    
        return sum(a[i] * b[i] for i in a if i in b)
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)