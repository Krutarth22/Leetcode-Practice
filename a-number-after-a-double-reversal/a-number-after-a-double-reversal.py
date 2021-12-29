class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if len(str(num)) == 1:
            return True
        
        ans = []
        num = str(num)
        
        for i in num:
            ans.append(i)
            
        if ans[-1] == "0":
            return False
        
        return True