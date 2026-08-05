class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i:i[1])

        ans = 0 
        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:

            if start < lastEnd:
                ans+=1 
            else:
                lastEnd = end
        
        return ans





            

           
        
        