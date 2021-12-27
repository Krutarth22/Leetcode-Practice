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
        
        
        begin = 0
        
        end = len(s) - 1
        
        while begin < end:
            
            if s[begin] == s[end]:
                
                begin+=1
                end-=1
                
            else:
                
                left = s[begin+1: end+1]
                right = s[begin:end]
                
                
                if left == left[::-1] or right==right[::-1]:
                    return True
                
                else:
                    return False