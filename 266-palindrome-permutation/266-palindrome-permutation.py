class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        ans = Counter(s)
        
        count = 0
        
        for i in ans:
            
            if ans[i] % 2 !=0:
                
                count+=1
                
        return count < 2