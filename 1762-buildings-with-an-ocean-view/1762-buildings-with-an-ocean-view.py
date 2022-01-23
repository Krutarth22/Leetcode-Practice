class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        
        result = []
        
        temp = 0
        
        for i in range(len(heights)-1,-1,-1):
            
            if heights[i] > temp:
                
                result.append(i)
                
                temp = heights[i]
                
        return reversed(result)