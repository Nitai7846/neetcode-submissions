class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i:i[0])
        ans = []
        ans.append(intervals[0])

        for start, end in intervals[1:]:

            lastEnd = ans[-1][1]

            if start <= lastEnd:
                lastEnd = max(end, lastEnd)
                ans[-1][1] = lastEnd 
            else:
                ans.append([start, end])
        
        return ans
                
                
                


        