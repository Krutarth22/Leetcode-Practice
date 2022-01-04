class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        h =[]
        sort = sorted(intervals)
        for i in sort:
            # need a new meeting room
            if h == [] or h[0] >i[0]:
                heapq.heappush(h,i[1])
            # don't need a new meeting room, just update the end time
            else:
                heapq.heapreplace(h,i[1])
        return len(h)