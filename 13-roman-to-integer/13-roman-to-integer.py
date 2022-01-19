class Solution:
    def romanToInt(self, s: str) -> int:
        
        ans = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        result = 0
        
        for i in range(0,len(s)-1):
            
            if ans[s[i]] < ans[s[i+1]]:
                result-=ans[s[i]]
            else:
                result+=ans[s[i]]
                
        return result + ans[s[-1]]
                
                