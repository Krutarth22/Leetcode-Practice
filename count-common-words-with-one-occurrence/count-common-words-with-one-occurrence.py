class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        ans1 = Counter(words1)
        ans2 = Counter(words2)
        
        count = 0
        for i in ans1:
            
            if i in ans2 and ans1[i] == 1 and ans2[i] == 1:
                count+=1
                
        return count