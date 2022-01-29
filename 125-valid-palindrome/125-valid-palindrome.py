class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == " ":
            return True
        
        ans = "".join(e for e in s if e.isalnum())
        
        ans = ans.lower()
        
        return ans== ans[::-1]
        