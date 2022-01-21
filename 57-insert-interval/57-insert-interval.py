class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        intervals.append(newInterval)

        result = []

        intervals.sort(key= lambda x: x[0])

        for i in intervals:
            if not result or result[-1][-1] < i[0]:
                result.append(i)
        
            else:
        
                result[-1][-1] = max(result[-1][-1], i[-1])
            
        return result