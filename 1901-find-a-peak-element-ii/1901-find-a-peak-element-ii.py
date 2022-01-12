class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        low = 0
        
        high = len(mat) - 1
        
        
        while low < high:
            
            mid = (low + high) // 2
            
            if max(mat[mid]) > max(mat[mid+1]):
                
                high = mid
                
            else:
                
                low = mid+1
                
                
        return [high, mat[high].index(max(mat[high])) ]