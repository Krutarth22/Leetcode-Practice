class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Step 1 sort the interval
        
        intervals.sort(key = lambda x: x[0])
        
        result = []
        
        
        for i in intervals:
            #if the list is empty or if there is no overlap, just append to the list
            if not result or result[-1][-1] < i[0]:
                
                result.append(i)
                
            else:
                #if there is overlap, append(max of the last element of list, i)
                result[-1][-1] = max(result[-1][-1], i[-1])
                
        return result