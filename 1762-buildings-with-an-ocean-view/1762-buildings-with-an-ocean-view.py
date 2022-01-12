class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        
        result = []
        
        height = 0
        
        for i in range(len(heights) -1,-1,-1):
            
            if heights[i] > height:
                
                result.append(i)
                
                height = heights[i]
                
                
        return reversed(result)