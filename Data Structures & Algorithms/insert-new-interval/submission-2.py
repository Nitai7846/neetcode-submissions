class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        n = len(intervals)

        new_start, new_end = newInterval 

        for i in range(n):

            old_start, old_end = intervals[i]

            if old_end < new_start:
                result.append(intervals[i])
            
            elif old_start > new_end:
                result.append([new_start, new_end])
                return result + intervals[i:]

            else:
                new_start = min(new_start, old_start)
                new_end = max(new_end, old_end)
            
        result.append([new_start, new_end])
        return result 

        


            
        