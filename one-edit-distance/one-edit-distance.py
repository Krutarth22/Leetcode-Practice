class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if s == t or abs(len(s) - len(t)) > 1:
            return False
        
        
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            
            if s[i] == t[j]:
                
                i+=1
                j+=1
                
            else:
                
                return s[i+1:] == t[j+1:] or s[i:] == t[j+1:] or s[i+1:] == t[j:]
            
            
        return True
        
        
        