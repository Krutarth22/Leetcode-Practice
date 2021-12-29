class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        seen = ""
        
        final = 0
        
        for c in s:
            if c not in seen:
                
                seen+=c
                
            else:
                
                seen= seen[seen.index(c) + 1:] + c
                
            final = max(final, len(seen))
            
        return final
                
                