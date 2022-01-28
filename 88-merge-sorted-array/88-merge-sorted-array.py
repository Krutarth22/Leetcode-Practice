class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        index = m+n -1
        
        pointer1 = m-1
        pointer2 = n-1
        
        while pointer1 >= 0 and pointer2 >=0:
            
            if nums1[pointer1] > nums2[pointer2]:
                
                nums1[index] = nums1[pointer1]
                pointer1-=1
                
                index-=1
                
            else:
                
                nums1[index] = nums2[pointer2]
                pointer2-=1
                index-=1
        
        if pointer2 > -1:
            
            nums1[0:pointer2+1] = nums2[0:pointer2+1]