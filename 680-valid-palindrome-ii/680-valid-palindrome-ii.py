class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #two pointer solution
        
        if len(s) == 0:
            return False
        
        if len(s) == 1:
            return True
        
        if s == s[::-1]:
            return True
        
        
        start = 0
        
        end = len(s) - 1
        
        while start < end:
            
            if s[start] == s[end]:
                
                start+=1
                end-=1
                
            else:
                
                left = s[start+1: end + 1]
                right = s[start:end]
                
                if left == left[::-1] or right==right[::-1]:
                    return True
                else:
                    return False
                
        