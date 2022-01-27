class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        stack = []
        
        count = 0
        
        for c in s:
            
            if c == '(':
                
                stack.append(c)
                
            else:
                
                if stack:
                    stack.pop()
                    
                else:
                    count+=1
                    
        if stack:
            count+=len(stack)
        
        return count
                