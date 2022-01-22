class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        def helper(start,end,inputstring):
            
            if start >= end:
                return
            
            
            inputstring[start], inputstring[end] = inputstring[end], inputstring[start]
            
            return helper(start+1, end-1, inputstring)
        
        
        return helper(0,len(s)-1, s)