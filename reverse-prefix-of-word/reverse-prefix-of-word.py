class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        if ch not in word:
            return word
        index = word.index(ch)
        
        final = word[:index+1]
        final = final[::-1]
        
        ans = word[index+1:]
        
        return final+ans